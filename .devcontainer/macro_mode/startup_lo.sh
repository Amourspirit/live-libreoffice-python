#/bin/sh
# install extensions
bash /tmp/res/scripts/ext.sh
# remove the lock file if it exists.
FILE_LOCK=$CONFIG_DIR/.config/libreoffice/4/.lock
if [ -f "$FILE_LOCK" ]; then
    rm "$FILE_LOCK"
fi
# run soffice after ext are installed
# soffice --headless --terminate_after_init &

# if using github codespace then add some aliases
if [ "$CODESPACES" == "true" ]; then
    git config --global alias.co "checkout"
    git config --global alias.br "branch"
    git config --global alias.ci "commit"
    git config --global alias.s "status -s"
    git config --global alias.type "cat-file -t"
    git config --global alias.dump "cat-file -p"
fi

echo "Startup Success!!!"
