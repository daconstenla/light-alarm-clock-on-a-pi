# server of the raspi alarm

## database init / reset

To initalise / reset the database using the following set of commands:

```bash
rm -rf pialarmclockdb.db migrations
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## running the server

```bash
# flask run
./setup.sh
```
