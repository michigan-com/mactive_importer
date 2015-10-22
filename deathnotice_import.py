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

__version__ = '0.0.1'

def sorted_nicely(_list):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(_list, key = alphanum_key)

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

    def __str__(self):
        return "<Obit Name: {}\nAd#: {}\nPost Date: {}\nImages: {}\nSiicode: {}>" \
            .format(self.full_name, self.ad_number, self.created_at, self.images, self.siicode)

    @property
    def image_str(self):
        return ';'.join(self.images)

    @property
    def sql_params(self):
        return [self.full_name, self.text, str(self.created_at), self.image_str, self.siicode, self.ad_number, self.subclass_code, self.first_name, self.last_name, self.publication]

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
        print("Inserting obit")
        with connection.cursor() as cursor:
            sql = """INSERT INTO `death_notices`
            (`fname`, `btext`, `bdate`, `image`, `siicode`, `adnum`, `subclass`,
             `firstname`, `lastname`, `publication`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, self.sql_params)

        connection.commit()

    def update(self, connection, record_id=None):
        """ Update an already existing obit in database """
        if record_id is None and self.record_id is None:
            raise Exception("To update an obit, you must supply its corresponding recordID")
        if record_id is None:
            record_id = self.record_id

        print("Updating obit")

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

    obits = parse_obits(fname, _date)
    for obit in obits:
        print(obit)

        obit.save(connection)

        print('-' * 50)
    #connection.commit()

