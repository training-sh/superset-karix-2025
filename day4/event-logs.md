```
docker exec -it superset_postgres bash
```

```
psql -U superset -d superset
```
press q button to exit from pgsql : prompt


```
\l
```
```
\c superset
```
```
\d logs
```
```
\dt;
```
```
select distinct(action) from logs;
```
```
SELECT id, dttm, action, user_id, LEFT(json, 120) AS json_snippet
FROM logs
ORDER BY dttm DESC
LIMIT 10;
```
```
SELECT dttm, user_id, json
FROM logs
WHERE action = ''
ORDER BY dttm DESC
LIMIT 10;
```
```
exit
```

```
docker exec -it superset-db psql -U superset -d superset
```

```
docker exec -it superset-db psql -U superset -d superset -c "SELECT id, action, dttm FROM log ORDER BY dttm DESC LIMIT 5;"
```

```
docker exec -it superset-db psql -U superset -d superset
```

