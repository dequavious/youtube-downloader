 #!/bin/sh
sudo pgrep -f docker > /dev/null || systemctl start docker
docker stop "yt_dl"
docker container rm "yt_dl"
