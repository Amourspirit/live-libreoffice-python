#/bin/sh
# install extensions
bash "$CONFIG_DIR/.tmp/res/scripts/ext.sh"

# run soffice after ext are installed
bash "$CONFIG_DIR/.tmp/res/scripts/lo_init.sh"

# remove the lock file if it exists.
FILE_LOCK=$CONFIG_DIR/.config/libreoffice/4/.lock
if [ -f "$FILE_LOCK" ]; then
    rm "$FILE_LOCK"
fi

# this next command does not work properly for some reason so it is added to devcontainer.json
# nohup bash /defaults/autostart > /var/log/autostart.log 2>&1 &

# if using github codespace then add some aliases
if [ "$CODESPACES" == "true" ]; then
    git config --local alias.co "checkout"
    git config --local alias.br "branch"
    git config --local alias.ci "commit"
    git config --local alias.s "status -s"
    git config --local alias.type "cat-file -t"
    git config --local alias.dump "cat-file -p"
fi

echo "Startup Success!!!"
