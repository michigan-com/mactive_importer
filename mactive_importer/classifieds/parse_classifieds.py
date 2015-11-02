import re
from datetime import datetime

from .classified import Classified
from ..parse_html import parse_content

def parse_classifieds(root, date):
    run_date_el = root.find('run-date')
    ads = run_date_el.findall('pub-code')
    print(len(ads))
    for ad in ads:
        yield parse_ad(ad.find('ad-type'), date)

def parse_ad(ad_element, date):
    ad_number_el = ad_element.find('ad-number')
    ad_number = ad_number_el.text.strip()

    subclass_code_el = ad_element.find('subclass-code')
    sub_class_num = int(subclass_code_el.text.strip().replace('i', ''))

    start_date_el = ad_element.find('start-date')
    end_date_el = ad_element.find('end-date')
    start_date = datetime.strptime(start_date_el.text.strip(), '%m/%d/%Y').date()
    end_date = datetime.strptime(end_date_el.text.strip(), '%m/%d/%Y').date()

    ad_content_el = ad_element.find('ad-content')
    text_of_ad, images = parse_content(ad_content_el.text)

    logo_phone_number = ad_element.find('logo_phone_number')
    if logo_phone_number is not None:
        text_of_ad += ' {}'.format(logo_phone_number.text.strip())

    # These elements are DEFAULT NULL in the db
    online_zip_el = ad_element.find('onlinezip')
    online_price_el = ad_element.find('onlineprice')
    online_title_el = ad_element.find('onlinetitle')
    online_zip = online_zip_el.text.strip() if online_zip_el else None
    online_price = online_price_el.text.strip() if online_price_el else None
    online_title = online_title_el.text.strip() if online_title_el else None

    # These elements are DEFAULT ''
    street_el = ad_element.find('StreetMap')
    zip_el = ad_element.find('ZipMap')
    city_el = ad_element.find('CityName')
    street = street_el.text.strip() if street_el else ''
    _zip = zip_el.text.strip() if zip_el else ''
    city = city_el.text.strip() if city_el else ''

    return Classified(ad_number=ad_number, sub_class_num=sub_class_num, text_of_ad=text_of_ad,
        date_posted=date, start_date=start_date, end_date=end_date, street=street,
        city=city, _zip=_zip, online_zip=online_zip, online_price=online_price,
        online_title=online_title)

def strip_invalid_stuff(content):
    """ Simulating the following perl regex replaces in Python

        perl -pi -e 's/\xC5|\xA0|\xBF|\x1F//g' classlive.txt

        # ad-description usually has bad characters
        perl -pi -e 's/<ad-description>.*<\/ad-description>//g' classlive.txt

        perl -pi -e 's/<Original Cost>.*<\/Original Cost>//g' classlive.txt
        perl -pi -e 's/<Total Adjustment>.*<\/Total Adjustment>//g' classlive.txt
        perl -pi -e 's/<First Date>.*<\/First Date>//g' classlive.txt
        perl -pi -e 's/<Last Date>.*<\/Last Date>//g' classlive.txt
        perl -pi -e 's/<# Times Run Wrong>.*<\/# Times Run Wrong>//g' classlive.txt
        perl -pi -e 's/<Ad-In-Error #>.*<\/Ad-In-Error #>//g' classlive.txt
        perl -pi -e 's/<\* AD-IN-ERROR INFORMATION \*>.*<\/\* AD-IN-ERROR INFORMATION \*>//g' classlive.txt
        perl -pi -e 's/<Sales Rep #>.*<\/Sales Rep #>//g' classlive.txt
        perl -pi -e 's/<\* ADJUSTMENT INFORMATION \* >.*<\/\* ADJUSTMENT INFORMATION \* >//g' classlive.txt
        perl -pi -e 's/<Party Responsible>.*<\/Party Responsible>//g' classlive.txt
        perl -pi -e 's/<Nature of Error>.*<\/Nature of Error>//g' classlive.txt
    """
    regexes = [
        u'\u00C5|\u00A0|\u00BF|\u001F',
        '<ad-description>.*<\/ad-description>',
        '<Original Cost>.*<\/Original Cost>',
        '<Total Adjustment>.*<\/Total Adjustment>',
        '<First Date>.*<\/First Date>',
        '<Last Date>.*<\/Last Date>',
        '<# Times Run Wrong>.*<\/# Times Run Wrong>',
        '<Ad-In-Error #>.*<\/Ad-In-Error #>',
        '<\* AD-IN-ERROR INFORMATION \*>.*<\/\* AD-IN-ERROR INFORMATION \*>',
        '<Sales Rep #>.*<\/Sales Rep #>',
        '<\* ADJUSTMENT INFORMATION \* >.*<\/\* ADJUSTMENT INFORMATION \* >',
        '<Party Responsible>.*<\/Party Responsible>',
        '<Nature of Error>.*<\/Nature of Error>'
    ]
    regex_str = '|'.join(['({})'.format(r) for r in regexes])
    return re.sub(regex_str, '', content)

if __name__ == '__main__':
    strip_invalid('')

