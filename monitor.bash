#!/bin/bash

# backup the cron tables
crontab -l > /tmp/crontab.original

# use them as the basis for new cron tables
cp /tmp/crontab.original /tmp/crontab.informer

# update cron to monitor the poller process and call the informer python code if the poller  process dies
echo "* * * * * activepoller=$(/bin/ps auwx | grep poller.py | wc -l) && if [[ $activepoller -lt 2 ]]; then /usr/bin/python3 /home/ubuntu/ddex-price-reservation-alert/informer.py ; crontab /tmp/crontab.original ; fi" >> /tmp/crontab.informer
crontab /tmp/crontab.informer && rm /tmp/crontab.informer
