# -*- coding: utf-8 -*-
import os
import pymysql

def connect(db_name=None):
    if db_name is None:
        raise Exception('Specify db_name to connect')

    return pymysql.connect(
        host=os.getenv('DN_HOST', 'localhost'),
        user=os.getenv('DN_USER', ''),
        password=os.getenv('DN_PASS', ''),
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8'
    )
