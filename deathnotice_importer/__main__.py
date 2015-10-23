# -*- coding: utf-8 -*-
import sys
import os
from datetime import date, datetime
import pymysql

from .parse_xml import parse_obits

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
    if len(sys.argv) > 2:
        _date = sys.argv[2]
        _date = datetime.strptime(_date, '%Y-%m-%d').date()

    inserted = 0
    updated = 0
    obits = parse_obits(fname, icons, _date)
    for obit in obits:
        obit.save(connection)
        print(obit)

        if obit.inserted:
            inserted += 1
        elif obit.updated:
            updated += 1

        print('-' * 50)

    print("Inserted: " + str(inserted))
    print("Updated: " + str(updated))
    #connection.commit()

