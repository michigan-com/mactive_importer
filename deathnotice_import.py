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
        `50.57.27.19:/mnt/nfs/docs/http-detroitnewspapers/mideathnotices/assets/images/dnimages/<YEAR>/<MONTH>/`.
"""
import os
import sys
from datetime import date
import pymysql
import xml.etree.ElementTree as ET

from strip_html import strip_tags

__version__ = '0.0.1'

if __name__ == '__main__':
    today = date.today()
    year = today.year
    month = today.month
    print("YEAR: " + str(year), "MONTH: " + str(month))

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
    tree = ET.parse(fname)
    root = tree.getroot()

    run_date_el = root.find('run-date')
    run_date = run_date_el.text.strip()
    print("Run Date: " + run_date)

    pub_codes = run_date_el.findall('pub-code')
    for pub_code in pub_codes:
        pcode = pub_code.text.strip()
        #print("Pub Code: " + pcode)

        ad_type_el = pub_code.find('ad-type')
        ad_type = ad_type_el.text.strip()
        #print("Ad Type: " + ad_type)

        subclass_code_el = ad_type_el.find('subclass-code')
        subclass_code = subclass_code_el.text.strip()
        #print("Subclass Code: " + subclass_code)

        ad_number_el = ad_type_el.find('ad-number')
        ad_number = ad_number_el.text.strip()
        #print("Ad Number: " + str(ad_number))

        fds_el = ad_type_el.find('FieldedDataSet')
        first_name = fds_el.find('DNfirstname').text.strip()
        last_name = fds_el.find('DNlastname').text.strip()
        full_name = ', '.join([last_name, first_name])
        publication = fds_el.find('publication').text.strip()

        #print("Full Name: " + full_name)
        #print("First Name: " + first_name)
        #print("Last Name: " + last_name)
        #print("Publication: " + publication)

        ad_content_el = ad_type_el.find('ad-content')
        ad_content = ad_content_el.text.strip()
        #print(ad_content)

        text, images = strip_tags(ad_content_el.text)
        #if images:
        #    print(images)
        print(text)

        print('-'*50)

