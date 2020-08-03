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

4. Set the reservation price:

```bash
sed -i "/reservationprice =/c\reservationprice = 398.5" bid-reservation-price-alert.py
# Note:
# The /c (or "change line") flag tells BASH to replace the whole line.
```

5. Run the following command:

```bash
/usr/bin/python3 /home/ubuntu/ddex-price-reservation-alert/bid-reservation-price-alert.py &
```

6. Check the /tmp/bid-reservation-price-alert.err log file for errors and ensure the script job is properly detached.
