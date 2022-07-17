## YouTube Downloader
### REQUIREMENTS
1. Open terminal in project directory.
2. Install all system requirements and required python packages:
```
$ bash scripts/install_requirements.sh
```
    
### STEPS TO RUN WEB APP

1. Open terminal in the project directory
2. Run web-app using:
```
$ bash scripts/run_web_app.sh
```
3. Open http://0.0.0.0:5000/ in browser

### STEPS TO HAVE WEB-APP ALWAYS RUNNING LOCALLY USING DOCKER
1. Open terminal in the project directory
2. Build the docker image, using:
```
$ bash scripts/docker/build_docker.sh
```
3. Run the docker image, using:
```
$ bash scripts/docker/run_docker.sh
```
4. The web-app can now be accessed at http://0.0.0.0:13882/ in browser and will always be accessible at that address
unless the docker container is closed
#### HOW TO CLOSE DOCKER CONTAINER
```
$ bash scripts/docker/close_docker.sh
```