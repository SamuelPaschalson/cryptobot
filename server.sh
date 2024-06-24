#!/bin/bash

# Define the process name or the command to run your server
PROCESS_NAME="gunicorn"
APP_NAME="main:app"
LOG_FILE="/server.log"
PORT=5000

# Check if the process is running
if ! pgrep -f $PROCESS_NAME > /dev/null
then
    echo "$(date): $PROCESS_NAME not running. Starting the server..." >> $LOG_FILE
    # cd /path/to/your/app
    $PROCESS_NAME $APP_NAME --bind 0.0.0.0:$PORT >> $LOG_FILE 2>&1 &
else
    echo "$(date): $PROCESS_NAME is running." >> $LOG_FILE
fi