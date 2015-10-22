# -*- coding: utf-8 -*-
"""
    deathnotice_importer
    ~~~~~~~~~~~~~~~~~~~~

    Parses an XML file and adds obituraties to our `death_notice` mySQL database.

    It starts by reading an XML file, usually named `deathnotices.txt`.
    Then it parses the XML file for obituaries from the mactive adbase management
    system.  It then saves the obits into our mySQL database.

    Finally it copies all associated images into its respective directory under
    the mideathnotices app, usually:
        `<legacy_vm_ip>:/mnt/nfs/docs/http-detroitnewspapers/mideathnotices/assets/images/dnimages/<YEAR>/<MONTH>/`.
"""
import os
import re
import sys
from datetime import date, datetime
import pymysql
import xml.etree.ElementTree as ET

from strip_html import strip_tags
from obit import Obit

__version__ = '0.0.1'

def parse_obits(fname, date=None):
    tree = ET.parse(fname)
    root = tree.getroot()

    run_date_el = root.find('run-date')
    run_date = run_date_el.text.strip()
    print(run_date)

    pub_codes = run_date_el.findall('pub-code')
    for pub_code in pub_codes:
        ad_type_el = pub_code.find('ad-type')

        subclass_code_el = ad_type_el.find('subclass-code')
        subclass_code = subclass_code_el.text.strip()

        ad_number_el = ad_type_el.find('ad-number')
        ad_number = ad_number_el.text.strip()

        fds_el = ad_type_el.find('FieldedDataSet')
        first_name = fds_el.find('DNfirstname').text.strip()
        last_name = fds_el.find('DNlastname').text.strip()
        full_name = ', '.join([last_name, first_name])
        publication = fds_el.find('publication').text.strip()

        ad_content_el = ad_type_el.find('ad-content')
        ad_content = ad_content_el.text.strip()

        text, images = strip_tags(ad_content_el.text)

        siicode = ""
        final_images = []
        for image in images:
            if image in icons:
                siicode = image
                continue

            if '_logo' in image:
                continue

            final_images.append(image)

        images = sorted_nicely(final_images)

        yield Obit(first_name, last_name, ad_number, publication, text, images, siicode, date, subclass_code)

def sorted_nicely(_list):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(_list, key = alphanum_key)


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
    obits = parse_obits(fname, _date)
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

