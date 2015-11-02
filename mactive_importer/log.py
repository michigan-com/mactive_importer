# -*- coding: utf-8 -*-
import os
import logging

#from loggly.handlers import HTTPSHandler

_LOGGLY_KEY = os.getenv('LOGGLY', False)

_fmt = "(%(name)s) %(filename)s:%(lineno)d: %(message)s"
logging.basicConfig(format=_fmt)
logger = logging.getLogger("mactive_importer")
logger.setLevel(logging.INFO)

if _LOGGLY_KEY:
    print("FOUND LOGGLY KEY, PIPING LOGS TO LOGGLY")
    _url = "/inputs/{}/tag/mactive_importer".format(_LOGGLY_KEY)
    _loggly_handler = logging.handlers.HTTPHandler("logs-01.loggly.com", _url, method="POST", secure=True)
    logger.addHandler(_loggly_handler)

