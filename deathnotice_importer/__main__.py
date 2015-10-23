# -*- coding: utf-8 -*-
import sys
import os
from datetime import date, datetime
import pymysql

from .parse_xml import parse_obits

DEST_IMG_DIR = '/cust/docs/http-detroitnewspapers/mideathnotices/assets/images/dnimages'
SRC_IMG_DIR = '/cust/scripts/death_notices/feeds'

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

    if len(sys.argv) <= 1:
        raise Exception("First argument to script must be the location of the XML file")

    fname = sys.argv[1]
    dest_img_dir = DEST_IMG_DIR
    src_img_dir = os.path.dirname(fname)
    if len(sys.argv) > 2: 
        dest_img_dir = sys.argv[2]
    if len(sys.argv) > 3:
        _date = sys.argv[3]
        _date = datetime.strptime(_date, '%Y-%m-%d').date()

    dest_img_dir = os.path.join(dest_img_dir, str(year), str(month))
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
    #connection.commit()

