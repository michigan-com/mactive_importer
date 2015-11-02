setx DN_HOST ""
setx DN_USER ""
setx DN_PASS ""
setx AWS_ACCESS_KEY_ID ""
setx AWS_SECRET_ACCESS_KEY ""

cd /d K:\Mactive\Web\nm_feeds\mactive_importer
python -m mactive_importer.deathnotices --s3 -f "..\deathnotices_rs\deathnotices.xml" -d mideathnotices/assets/images/dnimages %*

