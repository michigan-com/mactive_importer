Deathnotice Importer
====================

Get a copy of our production deathnotice database

```
mysqldump -h <db_ip> -u <user> -p death_notices > death_notice.sql
```

Restore copy, can use `schema.sql` if you want

```
mysqldump -h localhost -u <user> -p death_notices < schema.sql
```
