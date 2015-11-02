# Mactive Importer
Importer for all things Mactive at michigan.com (which is too many things)

# Install
```
mkvirtualenv mactive
pip install -r requirements.txt
```
Environment Variables
---------------------

* DN\_HOST : mySQL IP, default: 'localhost'
* DN\_DB : mySQL database name, default: 'death\_notices'
* DN\_USER : mySQL user name, default: ''
* DN\_PASS : mySQL user password, default: ''
* AWS\_ACCESS\_KEY\_ID : AWS S3 access key
* AWS\_SECRET\_ACCESS\_KEY : AWS Secret access key
* LOGGLY : Loggly API KEY when presetn will send logs to loggly

# Test
nosetest -s

# Run

## [Death Notices](https://github.com/michigan-com/mactive_importer/tree/master/mactive_importer/deathnotices)
```
python -m mactive_importer.deathnotices
```
