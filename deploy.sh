#!/bin/bash

# Source: https://www.deployhq.com/blog/what-is-a-deployment-script

# Exit on error
set -e

# Load environment variables
source .env

# Setting default environment, with an option to override (implement override later)
HOST="${HOST:-192.168.0.15}"
PORT="${PORT:-8080}"
FRONTEND_FOLDER="${FRONTEND_FOLDER:-./frontend}"
SILENT_LOGGING="${SILENT_LOGGING:-0}"

# Prints the company logo for copyright reasons (from logo.txt)
cat logo.txt

# Print deployment start
echo "Starting deployment..."

# Install dependencies
echo "Installing dependencies..."
npm install --production

# Build the application
echo "Building application..."
npm run build

# Run database migrations
echo "Running database migrations..."
npm run migrate

# Restart the application
echo "Restarting application..."
pm2 restart app

echo "Deployment completed successfully!"


