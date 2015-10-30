#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR

source ./env.sh
source $WORKON_HOME/deathnotices/bin/activate
python -m deathnotice_importer -f /cust/scripts/death_notices/feeds/deathnotices.txt -d mideathnotices/assets/images/dnimages --s3
