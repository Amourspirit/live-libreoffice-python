#/bin/sh
# install extensions
bash /tmp/res/scripts/ext.sh
# remove the lock file if it exists.
FILE_LOCK=$CONFIG_DIR/.config/libreoffice/4/.lock
if [ -f "$FILE_LOCK" ]; then
    rm "$FILE_LOCK"
fi
# run soffice after ext are installed
soffice --terminate_after_init &
# this next command does not work properly for some reason so it is added to devcontainer.json
# nohup bash /defaults/autostart > /var/log/autostart.log 2>&1 &
echo "Startup Success!!!"
