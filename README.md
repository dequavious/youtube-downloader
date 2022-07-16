### STEPS TO RUN WEB APP

1. Create virtual environment
```
$ python3 -m venv venv
```
2. Activate virtual environment
``` 
$ . venv/bin/activate
```
3. Install required packages
```
$ pip install -r requirements.txt
```
4. Run app.py
```
$ python3 wsgi.py
```
5. Open "http://0.0.0.0:5000/" in browser

### HAVE WEB-APP ALWAYS RUNNING LOCALLY USING DOCKER
#### PREREQUISITES
##### Docker

If not already installed, Docker can be installed using the following steps:
1. Update the package index:
```
$ sudo apt update
```
2. Install Docker:
```
$ sudo apt install docker
```
3. Verify installation:
```
$ docker -version
```
#### STEPS TO RUN
1. Once Docker is installed, you need to start the Docker daemon, using:
```
$ sudo systemctl start docker
```
2. Open terminal in the project directory
3. Build the docker image specified in the Dockerfile, using:
```
$ docker build --tag yt-dl-docker .
```
3. Run the docker image, using:
```
$ docker run --restart always -d -p 13882:13882 yt-dl-docker
```
4. Verify that the docker container is up and running by inspecting the list returned by:
```
$ docker ps
```
5. The web-app can now be accessed at "http://0.0.0.0:13882/" in browser and will always be accessible at that address
unless the docker container closed
#### STEPS TO CLOSE
1. To close the web-app, get the container id of the docker image from the list returned by running:
```
$ docker ps
```
2. Then close the docker container, using:
```
$ docker stop CONTAINER_ID
```