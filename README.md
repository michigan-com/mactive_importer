Deathnotice Importer
====================

Parses an XML file and adds obituraties to our `death_notice` mySQL database.

It starts by reading an XML file, usually named `deathnotices.txt`.
Then it parses the XML file for obituaries from the mactive adbase management
system.  It then saves the obits into our mySQL database.

Finally it copies all associated images into its respective directory under
the mideathnotices app, usually:
    `<legacy_vm_ip>:/mnt/nfs/docs/http-detroitnewspapers/mideathnotices/assets/images/dnimages/<YEAR>/<MONTH>/`.


Setup
-----

Get a copy of our production deathnotice database

```
mysqldump -h <db_ip> -u <user> -p death_notices > death_notice.sql
```

Restore copy, can use `schema.sql` if you want

```
mysql -h localhost -u <user> -p death_notices < schema.sql
```

Environment Variables
---------------------

* DN\_HOST : mySQL IP, default: 'localhost'
* DN\_DB : mySQL database name, default: 'death\_notices'
* DN\_USER : mySQL user name, default: ''
* DN\_PASS : mySQL user password, default: ''
* AWS\_ACCESS\_KEY\_ID : AWS S3 access key
* AWS\_SECRET\_ACCESS\_KEY : AWS Secret access key

Run
---

To parse and save obits for `today`

```
python -m deathnotice_importer -f <path to xml file>
```

To parse and save obits for a different date:

```
python -m deathnotice_importer -f <path to xml file> -d <path to img dir>
```

To parse and save to a specific folder

```
python -m deathnotice_impoter -f <path to xml file> -d <path to img dir>  --date <date in format: YEAR-MONTH-DAY, e.g.: 2015-10-20>
```

Send to S3

```
python -m deathnotice_importer --s3 -f <path to xml file> -d <path to img dir>
```

Test
---
nosetests

Tips
----

This script needs a date to add the obits.  If not date is provided the date today
is used.  Obits are considered unique by the ad number AND the date.  So an identical
ad number with a different date will be INSERTED and not UPDATED.

Query to determine whether to INSERT or UPDATE:

```
SELECT `recordID` FROM `death_notices` WHERE `adnum`=%s AND `bdate`=%s
```

Where `adnum` is the ad number and `bdate` is the date supplied to the script
