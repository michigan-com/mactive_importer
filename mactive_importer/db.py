# -*- coding: utf-8 -*-
import os
import pymysql

from .log import logger

def connect(db_name=None):
    if db_name is None:
        raise Exception('Specify db_name to connect')

    host = os.getenv('DN_HOST', 'localhost')
    user = os.getenv('DN_USER', '')
    password = os.getenv('DN_PASS', '')

    logger.info('<mySQL Host: {}\nDB: {}\nUser: {}\nPass: {}\n' \
            .format(host, db_name, user, password))

    connection = None
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8'
        )
    except Exception as err:
        logger.info(err)
        raise Exception("Failed to connect to database: {}".format(err))

    return connection
