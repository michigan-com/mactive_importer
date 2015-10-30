# -*- coding: utf-8 -*-
import logging
import loggly.handlers

logging.config.fileConfig('../loggly.conf')
logger = logging.getLogger('deathnotices')
