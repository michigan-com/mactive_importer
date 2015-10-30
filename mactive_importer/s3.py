# -*- coding: utf-8 -*-
from boto.s3.key import Key
from boto.s3.connection import S3Connection

def connect():
    """ Uses AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY env vars automatically """
    return S3Connection()

def bucket(connection, name="michigan-static"):
    b = connection.get_bucket(name)
    return Key(b)

def upload_file(bucket, src, dest):
    bucket.key = dest
    return bucket.set_contents_from_filename(src)
