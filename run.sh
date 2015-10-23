#!/bin/bash

source ./env.sh
source $WORKON_HOME/deathnotices/bin/activate
python -m deathnotice_importer -f /home/ebower/deathnotices/feeds/deathnotices.txt
