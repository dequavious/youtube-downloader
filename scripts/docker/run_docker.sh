 #!/bin/sh
parent_path=$( cd "$(dirname "${BASH_SOURCE[1]}")" ; pwd -P )
cd "$parent_path"

sudo pgrep -f docker > /dev/null || systemctl start docker
docker run --restart unless-stopped -d -p 13882:13882 --name yt_dl yt-dl-docker

