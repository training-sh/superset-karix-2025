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
sudo chmod -R 777 /root/final-day
```


```
docker compose build --no-cache superset celery_worker
```

```
docker compose up --build
```



Login into another terminal


```
cd final-day
```
Load superset example
```
docker   exec -it superset_app superset load_examples
```

Go to temp-mail web for mailrelay

https://temp-mail.org/en


And copy the email id for your reports

if it is mailpit, check in

http://localhost:8085 

in place of localhost, it must be your vm name/ip
