#!/bin/bash

# backup the cron tables
crontab -l > /tmp/crontab.original

# use them as the basis for new cron tables
cp /tmp/crontab.original /tmp/crontab.informer

# make a temporary BASH script to check for polling activity
cat << EOF > /tmp/informer.bash
activepoller=\$(/bin/ps auwx | grep poller.py | wc -l)
if [[ \$activepoller -lt 2 ]]
then
  /usr/bin/python3 /home/ubuntu/ddex-price-reservation-alert/informer.py
  crontab /tmp/crontab.original
fi
EOF

# update cron to monitor the poller process with informer.bash
echo "* * * * * /bin/bash /tmp/informer.bash 1>/tmp/informer.out 2>/tmp/informer.err" >> /tmp/crontab.informer
crontab /tmp/crontab.informer && rm /tmp/crontab.informer
