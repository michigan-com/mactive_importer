# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def __init__(self, first_name, last_name):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
        self.images = []
        self.first_name = first_name
        self.last_name = last_name

    def handle_starttag(self, tag, attrs):
        if tag == 'imgp' or tag == 'img':
            for attr in attrs:
                if attr[0] != 'src':
                    continue

                self.images.append(attr[1])
                break

    def handle_data(self, d):
        if d == '\n':
            return
        if self.last_name.lower() and d.lower() == self.last_name.lower():
            d = "{} ".format(d)
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed), self.images

def parse_content(html, first_name='', last_name=''):
    s = CustomHTMLParser(first_name, last_name)
    s.feed(html)
    return s.get_data()
