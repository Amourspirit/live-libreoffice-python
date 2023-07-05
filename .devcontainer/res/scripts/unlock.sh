#!/bin/sh
# kill soffice if it's running
pkill -SIGKILL soffice 2>/dev/null || true

# remove the lock file if it exists.
FILE_LOCK=$HOME/.config/libreoffice/4/.lock
if [ -f "$FILE_LOCK" ]; then
    rm "$FILE_LOCK"
fi
