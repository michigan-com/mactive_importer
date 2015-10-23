# -*- coding: utf-8 -*-
import os
from shutil import copy

class Obit(object):
    """ Data container for each obituary in the XML file. """
    def __init__(self, first_name, last_name, ad_number,  publication,
            text, images, siicode, created_at='', subclass_code='', record_id=None):
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

        self.inserted = False
        self.updated = False

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
            self.last_name, self.publication,
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

    def copy_images(self, src_dir, dest_dir):
        for img in self.images:
            src = os.path.join(src_dir, img)
            dest = os.path.join(dest_dir, img)

            if not os.path.exists(src):
                print('Img not found {}'.format(src))
                continue

            copy(src, dest)
            if os.path.exists(dest):
                print('Copied from {} to {}'.format(src, dest))
            else:
                print('Failed to copy to {}'.format(dest))

    def insert(self, connection):
        """ Insert new obituary into database """

        with connection.cursor() as cursor:
            sql = """INSERT INTO `death_notices`
            (`fname`, `btext`, `bdate`, `image`, `siicode`, `adnum`, `subclass`,
             `firstname`, `lastname`, `publication`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
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
                `publication`=%s
            WHERE recordID=%s"""
            params = self.sql_params
            params.append(record_id)
            cursor.execute(sql, params)

        connection.commit()

        self.updated = True

