#!/bin/bash

# Load environment variables
source .env

# Kill the runnig server
PID=$( ps aux | grep '[s]erver.py' | awk '{print $2}' )
PORT_RUNNING=$(cat port_text.txt)
HOST=${HOST:-127.0.0.1}
FOLDER=${FOLDER}

if [ -n "$PID" ]; then
    echo ""
    echo "Killing running server at http://$HOST:$PORT_RUNNING/help.html. Process number $PID"
    kill "$PID"

    # Wait until the process ends
    while kill -0 "$PID" 2>/dev/null; do
        sleep 5
    done
fi

# Run delploy.sh
cd "$FOLDER"
./deploy.sh