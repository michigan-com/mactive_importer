#!/bin/bash

source ./env.sh
workon deathnotices
python -m deathnotice_importer -f /home/ebower/deathnotices/feeds/deathnotices.txt
