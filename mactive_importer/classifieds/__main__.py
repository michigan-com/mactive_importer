# -*- coding: utf-8 -*-
import os
from xml.etree.ElementTree import XML
from argparse import ArgumentParser
from datetime import datetime

from .parse_classifieds import parse_classifieds, strip_invalid_stuff
from ..db import connect
from ..log import logger

# 1) Parse and insert into classifieds_live (check for dupe)
# - Get run date
# - /web-export/run-date/pub-code/ad-type/
# - in the <ad-type> element ./ad-number | ./start-date | ./end-date | ./subclass-code | ./ad-content | ./upsl-url0 | ./upsl-url1 | ./upsl-url2| ./upsl-url3| ./upsl-url4| ./upsl-url5| ./FieldedDataSet/StreetMap| ./FieldedDataSet/CityName| ./FieldedDataSet/ZipMap| ./FieldedDataSet/onlinezip| ./FieldedDataSet/onlinetitle| ./FieldedDataSet/onlineprice| ./FieldedDataSet/LogoPhoneNumber
#
#   XML Element -> column name
#   i)      <subclass-code> -> subclassnum
#           re.sub('i', '') in value, e.g. 80i -> 80
#   ii)     <*-date> -> *-date
#           Format like yyyy-mm-dd
#   iii)    (optional) <LogoPhoneNumber>
#           append to ad_text (see <ad-content>)
#   iv)     <ad-content> -> text_of_ad
#           strip HTML out of text_of_ad
#           append LogoPhoneNumber to end of text_of_ad (if necessary)
#           IMAGES - look for .eps.jpg
#           Currently copies to /cust/docs/http-detroitnewspapers/marketplacedetroit/adimages/$ad_text_image
#   v)      <onlinezip> -> onlinezip
#   vi)     <onlineprice> -> onlineprice
#   vii)    <onlinetitle> -> onlinetitle
#   viii)   <StreetMap> -> street
#   ix)     <ZipMap> -> zip
#   x)      <CityName> -> city
#   xi)     <ad-number> -> adnum
#   xii)    <run-date> -> date_posted
#           This is global in the XML file
#
#   hardcode source -> DNFP
#
# 2) Delete ???
    # DELETE   FROM classifieds_live
    # WHERE    run_days = '7'
    # AND  date_posted < DATE_SUB(CURRENT_DATE, INTERVAL 7 DAY)
#
#
#

DEST_IMG_DIR = 'marketplacedetroit/adimages'

parser = ArgumentParser(description='Parse Mactive Classifieds feed')
parser.add_argument('-f', dest='fname', help='Path to classifieds file to read from', required=True)

connection = connect(db_name='dbVerticals')

args = parser.parse_args()
fname = args.fname
src_img_dir = os.path.dirname(fname)

xml_content = ''
with open(fname) as fp:
    xml_content = strip_invalid_stuff(fp.read())

root = XML(xml_content)
run_date = root.find('run-date').text.strip()

_date = run_date
_date = datetime.strptime(_date, '%m/%d/%Y').date()

ads = parse_classifieds(root, _date)
inserted = 0
updated = 0
for ad in ads:
    logger.info(ad)
    ad.save(connection)

    if ad.insert:
        inserted += 1
    elif ad.update:
        updated += 1

logger.info('''
Processed Classifieds from {}

    Inserted: {}
    Updated: {}
'''.format(_date, inserted, updated))

connection.close()

