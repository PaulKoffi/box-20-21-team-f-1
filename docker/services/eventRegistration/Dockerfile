# set base image (host OS)
FROM python:3.8

LABEL djotiham (SOA 2020)

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY resources/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY resources/src/ .

# Creating an health check verification to check rocket status
# HEALTHCHECK --interval=30s --timeout=30s CMD curl --fail http://localhost:7000/ || exit 1

# port
EXPOSE 2000

# command to run on container start
CMD [ "python", "./run.py" ]
# ENTRYPOINT [ "python", "./run.py" ]
