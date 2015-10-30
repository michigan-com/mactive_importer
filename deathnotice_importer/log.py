# -*- coding: utf-8 -*-
import os
import logging
import loggly.handlers

PACKAGE_DIR = os.path.join(os.path.dirname(__file__), os.pardir)

logging.config.fileConfig(os.path.join(PACKAGE_DIR, 'loggly.conf'))
logger = logging.getLogger('deathnotices')
