## Setup Guide

To execute, fire up an EC2 instance running Ubuntu 18.04.4 LTS (GNU/Linux 5.3.0-1023-aws x86_64):

1. Create a hidden aws directory in your home directory:

```bash
mkdir ~/.aws
```

2. Create a config file for Amazon Web Services:

```bash
cat > ~/.aws/config
[default]
region=us-east-1
[CTRL-D]
```

3. Create a credentials file for Amazon Web Services:

```bash
cat > ~/.aws/credentials
[default]
aws_access_key_id = XXXXX
aws_secret_access_key = XXXXX
[CTRL-D]
```

4. Choose your poller:

```bash
cp /home/ubuntu/ddex/poller/bid-reservation-price-alert.py poller.py
```

5. Set the reservation price:

```bash
sed -i "/reservationprice =/c\reservationprice = 398.5" poller.py
# Note:
# The /c (or "change line") flag tells BASH to replace the whole line.
```

6. Run the following command:

```bash
nohup /usr/bin/python3 /home/ubuntu/ddex/poller.py &
```

7. Check the /tmp/poller.err log file for errors and ensure the script job is properly detached:

```bash
tail -f /tmp/poller.err
```

8. Run monitor.bash to get an alert the minute the poller process dies:

```bash
bash monitor.bash
```
