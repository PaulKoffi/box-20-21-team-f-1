# set base image (host OS)
FROM python:3.8

MAINTAINER djotiham (SOA 2020)

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY resources/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY resources/socketPayloadTelemetriesServer.py .

# Creating an health check verification to check rocket status
# HEALTHCHECK --interval=30s --timeout=30s CMD curl --fail http://localhost:9292/ || exit 1

# port
EXPOSE 9292

# command to run on container start
CMD [ "python", "./socketPayloadTelemetriesServer.py" ]
# ENTRYPOINT [ "python", "./run.py" ]