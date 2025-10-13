# REDHAT SETUP

```
vi Dockerfile
```

```
vi docker-compose.yml
```


```
vi superset_config.py
```

```
docker compose build --no-cache superset celery_worker
```
```
docker compose up --build
```

open browser, 

```
http://yourvm-ip:8088
```

```
username: admin
password: admin
```

