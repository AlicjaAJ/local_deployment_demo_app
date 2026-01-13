#!/bin/bash

# Source: https://www.deployhq.com/blog/what-is-a-deployment-script

# Exit on error
set -e

# Load environment variables
source .env

PORT=${PORT:-8080}

# Allows for manual overriding PORT by using syntax ./deploy.sh -port XXXX
if [ "$1" == "-port" ]; then
    PORT="$2"
fi

# Prints the company logo for copyright reasons (from logo.txt)
cat logo.txt
echo ""
echo ""

# Print deployment start
echo "Starting deployment..."
echo ""

# Install dependencies
echo "Installing dependencies..."
npm install --production

# Starts http server
./server.py -port "$PORT" &

# 10 seconds delay
sleep 10

# Run tests for API stored in response.py
echo ""
echo "Strating API test."
python3 response.py

echo ""
echo "Deployment completed successfully!"


