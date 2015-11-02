
class Classified():
    # Variable Name | Column name
    # ----------------------------
    # ad_number     | adnum
    # sub_class_num | subclassnum
    # text_of_ad    | text_of_ad
    # date_posted   | date_posted
    # start_date    | start-date
    # end_date      | end-date
    # street        | street
    # city          | city
    # _zip          | zip
    # online_zip    | onlinezip
    # online_price  | onlineprice
    # online_title  | onlinetitle
    # source        | source
    def __init__(self, ad_number, sub_class_num, text_of_ad, date_posted, start_date,
            end_date, street, city, _zip, online_zip, online_price, online_title,
            source='DNFP'):
        self.ad_number = ad_number
        self.sub_class_num = sub_class_num
        self.text_of_ad = text_of_ad
        self.date_posted = date_posted
        self.start_date = start_date
        self.end_date = end_date
        self.street = street
        self.city = city
        self._zip = _zip
        self.online_zip = online_zip
        self.online_price = online_price
        self.online_title = online_title
        self.source = source

        self.insert = False
        self.update = False

    @property
    def sql_params(self):
        return [
            self.ad_number, self.sub_class_num, self.text_of_ad, self.date_posted,
            self.start_date, self.end_date, self.street, self.city, self._zip, self.online_zip,
            self.online_price, self.online_title, self.source
        ]

    def find(self, connection):
        with connection.cursor() as cursor:
            sql = 'SELECT `adnum` FROM `classifieds_live` where `adnum`=%s'
            cursor.execute(sql, (self.ad_number))
            result = cursor.fetchone()

            if result is None:
                self.insert = True
                self.update = False
            else :
                self.update = True
                self.insert = False

    # Insert or update
    def save(self, connection):
        self.find(connection)

        with connection.cursor() as cursor:
            if self.insert:
                sql = '''INSERT INTO `classifieds_live`
                (`adnum`, `subclassnum`, `text_of_ad`, `date_posted`, `start-date`, `end-date`,
                `street`, `city`, `zip`, `onlinezip`, `onlineprice`, `onlinetitle`, `source`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cursor.execute(sql, self.sql_params)
            elif self.update:
                sql = '''UPDATE `classifieds_live`
                SET `adnum`=%s, `subclassnum`=%s, `text_of_ad`=%s, `date_posted`=%s, `start-date`=%s,
                    `end-date`=%s, `street`=%s, `city`=%s, `zip`=%s, `onlinezip`=%s, `onlineprice`=%s,
                    `onlinetitle`=%s, `source`=%s
                WHERE `adnum`=%s'''

                params = self.sql_params
                params.append(self.ad_number)
                cursor.execute(sql, params)


