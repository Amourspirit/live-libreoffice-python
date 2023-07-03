#!/bin/sh
echo "Reloading..."
if pgrep tint2 > /dev/null; then
    pkill -SIGKILL tint2
fi
nohup bash /defaults/autostart >> /var/log/autostart.log 2>&1
echo "Reloaded!"