#!/bin/bash

# backup the cron tables
crontab -l > /tmp/crontab.original

# use them as the basis for new cron tables
cp /tmp/crontab.original /tmp/crontab.informer

# make a temporary BASH script to check for polling activity
echo "activepoller=$(/bin/ps auwx | grep poller.py | wc -l) && if [[ $activepoller -lt 2 ]]; then exit 1 ; fi" > /tmp/informer.bash

# update cron to run this shell script every minute and call the informer python code if the poller  process dies
echo "* * * * * bash /tmp/informer.bash || /usr/bin/python3 /home/ubuntu/ddex/informer.py" >> /tmp/crontab.informer
crontab /tmp/crontab.informer && rm /tmp/crontab.informer
