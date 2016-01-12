# -*- coding: utf-8 -*-
import sys
import os
from datetime import date, datetime
import xml.etree.ElementTree as ET
from argparse import ArgumentParser

import pymysql

from .parse_xml import parse_obits
#from .send_email import send_email
from ..db import connect
from ..log import logger

DEST_IMG_DIR = 'mideathnotices/assets/images/dnimages'
SRC_IMG_DIR = '/cust/scripts/death_notices/feeds'

parser = ArgumentParser(description='Parse Mactive Deathnotice feeds')
parser.add_argument('-f', dest='fname', help='Path to obit XML file to read from', required=True)
parser.add_argument('-d', dest='dest', help='Path to destination directory for images', default=DEST_IMG_DIR)
parser.add_argument('--date', dest='date', help='YYYY-MM-DD date string, specifying the specific day to process', default="")
parser.add_argument('--s3', dest='use_s3', help='Flag to attempt to upload to AWS S3', action='store_true', default=False)

if __name__ == '__main__':
    icons = []
    #TODO: turn this into a db table
    with open(os.path.join(os.path.dirname(__file__), 'dn_icons.txt'), 'r') as fp:
        icons = fp.read().splitlines()

    connection = connect(db_name='death_notices')

    args = parser.parse_args()
    fname = args.fname
    src_img_dir = os.path.dirname(fname)
    input_date = args.date
    use_s3 = args.use_s3

    tree = ET.parse(fname)
    root = tree.getroot()
    run_date = root.find('run-date').text.strip()

    _date = run_date #datetime.utcnow().date()
    _date = datetime.strptime(_date, '%m/%d/%Y').date()
    if input_date:
        _date = input_date
        _date = datetime.strptime(_date, '%Y-%m-%d').date()

    year = _date.year
    month = _date.month

    dest_img_dir = "/".join([args.dest, str(year), str(month)])

    #if not os.path.exists(dest_img_dir):
    #    os.makedirs(dest_img_dir)

    inserted = 0
    updated = 0
    img_success = 0
    img_fail = 0

    obits = parse_obits(root, use_s3, icons, _date)
    for obit in obits:
        obit.save(connection)
        obit.copy_images(src_img_dir, dest_img_dir)
        logger.info(obit)

        if obit.inserted:
            inserted += 1
        elif obit.updated:
            updated += 1

        if obit.img_copy == 1:
            img_success += 1
        elif obit.img_copy == -1:
            img_fail += 1

    connection.commit()

    msg = """Inserted: {}\n
    Updated: {}\n
    Img Copy Success: {}\n
    Img Copy Fail: {}""".format(
        str(inserted), str(updated),
        str(img_success), str(img_fail)
    )

    logger.info(msg)
    connection.close()
    #send_email(msg)

