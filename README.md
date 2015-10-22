Deathnotice Importer
====================

Setup
-----

Get a copy of our production deathnotice database

```
mysqldump -h <db_ip> -u <user> -p death_notices > death_notice.sql
```

Restore copy, can use `schema.sql` if you want

```
mysqldump -h localhost -u <user> -p death_notices < schema.sql
```

Environment Variables
---------------------

* DN\_HOST : mySQL IP, default: 'localhost'
* DN\_DB : mySQL database name, default: 'death\_notices'
* DN\_USER : mySQL user name, default: ''
* DN\_PASS : mySQL user password, default: ''

Run
---

To parse and save obits for `today`

```
python deathnotice_importer.py <deathnotices_xml_file>
```

To parse and save obits for a different date:

```
python deathnotice_importer.py <deathnotices_xml_file> <date in format: YEAR-MONTH-DAY, e.g.: 2015-10-20>
```
