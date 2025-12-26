#!/bin/bash

# Source: https://www.deployhq.com/blog/what-is-a-deployment-script

# Exit on error
set -e

# Load environment variables
source .env

# Prints the company logo for copyright reasons (from logo.txt)
cat logo.txt
echo ""
echo ""

# Print deployment start
echo "Starting deployment..."
echo ""

# Starts http server
./server.py &

# 10 seconds delay
sleep 10

# Run tests for API stored in response.py
echo "Strating API test."
python3 response.py

# Install dependencies
echo "Installing dependencies..."
npm install --production


echo "Deployment completed successfully!"


