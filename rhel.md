need to consolidate.. but worked so far..

change due to space limit in /var by vendor vm

```
docker info | grep "Docker Root Dir"

 
sudo docker system prune -a
 
sudo systemctl stop docker

 
ls  /var/lib/docker
 
sudo mv /var/lib/docker /root/docker-data
 
sudo mkdir -p /etc/docker
 
sudo tee /etc/docker/daemon.json <<EOF
{
  "data-root": "/root/docker-data"
}
EOF
 
 
sudo cat /etc/docker/daemon.json
 
sudo systemctl start docker
 
docker info
```
 
