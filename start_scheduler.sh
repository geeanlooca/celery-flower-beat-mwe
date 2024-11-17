#!/bin/sh

# Start Celery Beat in the background
celery -A tasks beat --loglevel=info &

# Store the PID of the beat process
BEAT_PID=$!

# Start Flower in the foreground with proper host binding
celery -A tasks flower --port=${FLOWER_WEBUI_PORT} --host=0.0.0.0

# If Flower exits, kill Beat
kill $BEAT_PID
