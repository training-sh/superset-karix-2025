# Reports and Alerts config working

you may stop existing or remove existing containers
on the root directory

on root directory
```
docker compose down -v
```

```
cd day5
```

```
docker compose down -v
```

```
cd ~
``` 

```
wget  https://github.com/training-sh/superset-karix-2025/raw/refs/heads/main/final-day/final-day.zip

 ```


```
unzip final-day
```

```
cd final-day
```

```
docker compose build --no-cache superset celery_worker
```

```
docker compose up --build
```


```
docker   exec -it superset_app superset load_examples
```



