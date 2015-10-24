# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
        self.images = []
        self.last_tag = ''

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag == 'imgp' or tag == 'img':
            for attr in attrs:
                if attr[0] != 'src':
                    continue

                self.images.append(attr[1])
                break

    def handle_data(self, d):
        if d == '\n':
            return
        if self.last_tag == 'font':
            d = '{} '.format(d.strip())
        self.fed.append(d)

        self.last_tag = ''

    def get_data(self):
        return ''.join(self.fed), self.images

def parse_content(html):
    s = CustomHTMLParser()
    s.feed(html)
    return s.get_data()
