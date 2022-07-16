## YouTube Downloader
### REQUIREMENTS
1. Open terminal in project directory.
2. Install all system requirements:
```
$ bash scripts/requirements/install.sh
```
3. Create a virtual environment and install required packages, using:
```
$ bash scripts/requirements/setup.sh
```
    
### STEPS TO RUN WEB APP

1. Open terminal in the project directory
2. Activate virtual environment
``` 
$ . venv/bin/activate
```
3. Run app.py
```
$ python3 wsgi.py
```
4. Open http://0.0.0.0:5000/ in browser

### STEPS TO HAVE WEB-APP ALWAYS RUNNING LOCALLY USING DOCKER
1. Open terminal in the project directory
2. Build the docker image, using:
```
$ bash scripts/docker/build.sh
```
3. Run the docker image, using:
```
$ bash scripts/docker/run.sh
```
4. The web-app can now be accessed at http://0.0.0.0:13882/ in browser and will always be accessible at that address
unless the docker container is closed
#### HOW TO CLOSE DOCKER CONTAINER
```
$ bash scripts/docker/close.sh
```