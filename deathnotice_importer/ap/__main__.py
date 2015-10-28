# -*- coding: utf-8 -*-
""" Primary entry point for grabbing Associated Press obits. """
from datetime import datetime
import xml.etree.ElementTree as ET

import requests
import pymysql

def get_xml(url="http://hosted.ap.org/lineups/OBIT-rss_2.0.xml?SITE=MIDTN"):
    resp = requests.get(url)
    print(resp.url)
    resp.raise_for_status()

    return ET.fromstring(resp.content)

if __name__ == '__main__':
    root = get_xml()

    #channel_el = root.find('channel')
    obits = root.findall('channel/item')
    for obit in obits:
        title_el = obit.find('title')
        title = title_el.text.strip()
        print(title)

        link_el = obit.find('link')
        link = link_el.text.strip()
        print(link)

        desc_el = obit.find('description')
        desc = desc_el.text.strip()
        print(desc)

        str_date = obit.find('pubDate').text.strip()
        #Tue, 27 Oct 2015 20:26:34 GMT
        date = datetime.strptime(str_date, "%a, %d %b %Y %H:%M:%S %Z").date()
        print(str(date))

        print('----')

