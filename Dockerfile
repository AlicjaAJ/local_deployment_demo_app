# Set the version
# Start your image with a node base image
FROM node:18

# Sets the work directory
WORKDIR /app

# Copy content of frontend to a local container
COPY . /app

RUN npm install

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip
RUN pip install --break-system-packages -r requirements.txt

# Make script executable
RUN chmod +x server.py response.py
RUN chmod +x deploy.sh deploy_cron.sh

# Set environmetnal variables
ENV PORT=8080
ENV HOST=127.0.0.1
ENV LOGGING=1

# Start the deployment
CMD ["./deploy.sh"]

