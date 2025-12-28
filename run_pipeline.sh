#!/bin/bash
set -e  # stop if any command fails
LOG_FILE="/Users/matthew/insights-generator/cron.log"
VENV_PY="/Users/matthew/insights-generator/venv/bin/python"
BASE="/Users/matthew/insights-generator"

# Function to log with timestamp
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

log "Pipeline started."
$VENV_PY "$BASE/main.py"
log "Pipeline finished."