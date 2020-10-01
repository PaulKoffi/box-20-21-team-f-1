# set base image (host OS)
FROM python:3.8

MAINTAINER djotiham (SOA 2020)

# set the working directory in the container
WORKDIR /code

# install dependencies
RUN pip install requests

# copy the content of the local src directory to the working directory
COPY resources/pollcreator.py .

# Creating an health check verification to check pollcreator status
HEALTHCHECK --interval=30s --timeout=30s CMD curl --fail http://localhost:9000/ || exit 1

# port
EXPOSE 9000

# command to run on container start
CMD [ "python", "./pollcreator.py" ]