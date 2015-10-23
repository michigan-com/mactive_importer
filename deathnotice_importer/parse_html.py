# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
        self.images = []

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
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed), self.images

def parse_content(html):
    s = CustomHTMLParser()
    s.feed(html)
    return s.get_data()
