# set base image (host OS)
FROM python:3.8

MAINTAINER djotiham (SOA 2020)

# set the working directory in the container
WORKDIR /code

# install dependencies
RUN pip install requests

# copy the content of the local src directory to the working directory
COPY resources/toryCLI.py .

# command to run on container start
CMD [ "python", "./toryCLI.py" ]