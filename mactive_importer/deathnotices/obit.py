# -*- coding: utf-8 -*-
import os
from shutil import copy
from datetime import date

from ..s3 import *
from ..log import logger

class Obit(object):
    """ Data container for each obituary in the XML file. """
    def __init__(self, first_name, last_name, ad_number,  publication,
            text, images, siicode, created_at='', subclass_code='', record_id=None, use_s3=False):
        self.record_id = record_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = ', '.join([last_name, first_name])
        self.ad_number = ad_number
        self.publication = publication
        self.text = text.encode('utf-8')
        self.images = images
        self.siicode = siicode
        self.subclass_code = subclass_code
        if not created_at:
            created_at = date.today()
        self.created_at = created_at

        if use_s3:
            self.use_s3 = 1
        else:
            self.use_s3 = 0

        self.inserted = False
        self.updated = False
        self.img_copy = 0

    def __str__(self):
        return "<Obit Name: {}\nAd#: {}\nPost Date: {}\nImages: {}\nSiicode: {}>" \
            .format(self.full_name, self.ad_number, self.created_at, self.images, self.siicode)

    @property
    def image_str(self):
        return ';'.join(self.images)

    @property
    def sql_params(self):
        return [
            self.full_name, self.text, str(self.created_at), self.image_str,
            self.siicode, self.ad_number, self.subclass_code, self.first_name,
            self.last_name, self.publication, self.use_s3,
        ]

    def find(self, connection):
        """ Find the record in our database """
        with connection.cursor() as cursor:
            sql = "SELECT `recordID` FROM `death_notices` WHERE `adnum`=%s AND `bdate`=%s"
            cursor.execute(sql, (self.ad_number, self.created_at))
            result = cursor.fetchone()

            if result is None:
                return None

            self.record_id = result['recordID']
            return self.record_id

    def save(self, connection):
        self.find(connection)

        if self.record_id is not None:
            self.update(connection)
        else:
            self.insert(connection)

    def insert(self, connection):
        """ Insert new obituary into database """

        with connection.cursor() as cursor:
            sql = """INSERT INTO `death_notices`
            (`fname`, `btext`, `bdate`, `image`, `siicode`, `adnum`, `subclass`,
             `firstname`, `lastname`, `publication`, `iss3`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, self.sql_params)

        connection.commit()

        self.inserted = True

    def update(self, connection, record_id=None):
        """ Update an already existing obit in database """
        if record_id is None and self.record_id is None:
            raise Exception("To update an obit, you must supply its corresponding recordID")
        if record_id is None:
            record_id = self.record_id

        with connection.cursor() as cursor:
            sql = """UPDATE `death_notices`
            SET `fname`=%s, `btext`=%s, `bdate`=%s, `image`=%s, `siicode`=%s,
                `adnum`=%s, `subclass`=%s, `firstname`=%s, `lastname`=%s,
                `publication`=%s, `iss3`=%s
            WHERE recordID=%s"""
            params = self.sql_params
            params.append(record_id)
            cursor.execute(sql, params)

        connection.commit()

        self.updated = True

    def copy_images(self, src_dir, dest_dir):
        connection = None
        bucket = None
        if self.use_s3:
            connection = s3.connect()
            bucket = s3.bucket(connection)

        for img in self.images:
            src = os.path.join(src_dir, img)
            dest = "/".join([dest_dir, img])

            if not os.path.exists(src):
                logger.info('Img not found {}'.format(src))
                continue

            if self.use_s3:
                try:
                    self.img_copy = 1
                    s3.upload_file(bucket, src, dest)
                    logger.info('[S3] Copied from local {} to S3 michigan-static/{}'.format(src, dest))
                except Exception as e:
                    self.img_copy = -1
                    logger.info(e)
                    logger.info('[S3] Failed to copy to S3 michigan-static/{}'.format(src, dest))
            else:
                try:
                    copy(src, dest)
                    self.img_copy = 1
                    logger.info('Copied from {} to {}'.format(src, dest))
                except Exception as e:
                    self.img_copy = -1
                    logger.info(e)
                    logger.info('Failed to copy to {}'.format(dest))

