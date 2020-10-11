FROM node:10
MAINTAINER djotiham (SOA 2020)

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY resources/package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY resources/. .

# Creating an health check verification to check weather status
# HEALTHCHECK --interval=30s --timeout=30s CMD curl --fail http://localhost:7S000/ || exit 1

EXPOSE 7000
CMD [ "node", "app.js" ]
