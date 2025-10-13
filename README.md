# REDHAT SETUP

Change docker default location..  


```
sudo mkdir -p /etc/docker
```

```
sudo tee /etc/docker/daemon.json <<EOF
{
  "data-root": "/root/docker-data"
}
EOF
```

```
sudo cat /etc/docker/daemon.json
```

Install docker

```
sudo dnf -y install dnf-plugins-core
```

```
sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
```

```
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```
sudo systemctl enable --now docker
```
 
``` 
sudo docker run hello-world
```
 
```
sudo groupadd docker
```

```
sudo usermod -aG docker $USER
```

```
newgrp docker
```

copy and save files into respective locations..

``` 
vi Dockerfile
```

```
vi docker-compose.yml
```

```
vi superset_config.py
```

need to change the path before running below cmd:

``` 
docker compose build --no-cache superset celery_worker
```

we are running docker containers on shell prompt itself, fore ground. you may run in backgroun after all setup working..


```
chmod -R a+r /root
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

run below commands in differnt ssh to your vm..


check your vm space /

```
df -h
```

check your vm memory
```
df -h
```

```

