#!/bin/bash

# Source: https://www.deployhq.com/blog/what-is-a-deployment-script

# Exit on error
set -e

# Load environment variables
source .env

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


