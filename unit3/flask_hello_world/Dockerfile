# our base image
FROM ubuntu:latest

# Install python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# upgrade pip
RUN pip3 install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY hello_world.py /usr/src/app/
COPY Procfile /usr/src/app/
COPY runtime.txt /usr/src/app/
COPY templates/* /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 80

# run the application
CMD ["python3", "/usr/src/app/hello_world.py"]
