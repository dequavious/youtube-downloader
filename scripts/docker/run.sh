parent_path=$( cd "$(dirname "${BASH_SOURCE[1]}")" ; pwd -P )
cd "$parent_path"

sudo systemctl start docker
docker run --restart always -d -p 13882:13882 --name yt_dl yt-dl-docker

