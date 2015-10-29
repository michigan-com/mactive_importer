# -*- coding: utf-8 -*-
import os
import re
import xml.etree.ElementTree as ET

from .parse_html import parse_content
from .obit import Obit

def parse_obits(root, icons=[], date=None):
    run_date_el = root.find('run-date')
    run_date = run_date_el.text.strip()
    print(run_date)

    pub_codes = run_date_el.findall('pub-code')
    for pub_code in pub_codes:
        yield get_obit(pub_code, icons, date)

def get_obit(pub_code, icons=[], date=None):
    """ Parse out an Obit given a <pub-code> XML element """
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

    text, images = parse_content(ad_content_el.text, first_name, last_name)

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
    return Obit(first_name, last_name, ad_number, publication, text, images, siicode, date, subclass_code, use_s3=os.getenv('USE_S3', 0))

def sorted_nicely(_list):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(_list, key = alphanum_key)

