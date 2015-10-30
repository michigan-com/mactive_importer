setx DN_HOST ""
setx DN_USER ""
setx DN_PASS ""
setx AWS_ACCESS_KEY_ID ""
setx AWS_SECRET_ACCESS_KEY ""

cd "C:\Program Files\feeds\deathnotices\deathnotice_importer"
python -m deathnotice_importer --s3 -f "C:\Program Files\feeds\deathnotices\feeds\deathnotices.txt" -d mideathnotices/assets/images/dnimages %*
