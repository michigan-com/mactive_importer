# -*- coding: utf-8 -*-
import sys
import os
from datetime import date, datetime
from argparse import ArgumentParser

import pymysql

from .parse_xml import parse_obits

DEST_IMG_DIR = '/cust/docs/http-detroitnewspapers/mideathnotices/assets/images/dnimages'
SRC_IMG_DIR = '/cust/scripts/death_notices/feeds'

parser = ArgumentParser(description='Parse Mactive Deathnotice feeds')
parser.add_argument('-f', dest='fname', help='Path to obit XML file to read from', required=True)
parser.add_argument('-d', dest='dest', help='Path to destination directory for images', default=DEST_IMG_DIR)
parser.add_argument('--date', dest='date', help='YYYY-MM-DD date string, specifying the specific day to process', default="")

if __name__ == '__main__':
    _date = date.today()
    year = _date.year
    month = _date.month

    print("YEAR: " + str(year), "MONTH: " + str(month))

    icons = []
    #TODO: turn this into a db table
    with open('dn_icons.txt', 'r') as fp:
        icons = fp.read().splitlines()

    connection = pymysql.connect(
        host=os.getenv('DN_HOST', 'localhost'),
        user=os.getenv('DN_USER', ''),
        password=os.getenv('DN_PASS', ''),
        db=os.getenv('DN_DB', 'death_notices'),
        cursorclass=pymysql.cursors.DictCursor,
    )

    args = parser.parse_args()
    fname = args.fname
    dest_img_dir = os.path.join(args.dest, str(year), str(month))
    src_img_dir = os.path.dirname(fname)
    input_date = args.date

    if input_date:
        _date = input_date
        _date = datetime.strptime(_date, '%Y-%m-%d').date()

    if not os.path.exists(dest_img_dir):
        os.makedirs(dest_img_dir)

    inserted = 0
    updated = 0
    obits = parse_obits(fname, icons, _date)
    for obit in obits:
        obit.save(connection)
        obit.copy_images(src_img_dir, dest_img_dir)
        print(obit)

        if obit.inserted:
            inserted += 1
        elif obit.updated:
            updated += 1

        print('-' * 50)

    print("Inserted: " + str(inserted))
    print("Updated: " + str(updated))
    connection.commit()

