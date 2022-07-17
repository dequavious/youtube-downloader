 #!/bin/sh
sudo pgrep -f docker > /dev/null || systemctl start docker
docker build --tag yt-dl-docker .