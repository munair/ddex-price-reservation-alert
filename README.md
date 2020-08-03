To execute:

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
```

4. Set the reservation price:

```bash
sed -i "/^reservationprice =/c\reservationprice = 398.5" bid-reservation-price-alert.py
# Note:
# The /c (or "change line") flag tell BASH to replace the whole line.
# The caret (^) matches the beginning of a line.
# It is unnecessary here, but is included for safety.
```

5. Create a cronjob:

```bash
crontab -e 0/2 0 0 ? * * * >/dev/null bid-reservation-price-alert.py 2>&1
```

6. Check the /tmp/bid-reservation-price-alert.err log file for errors and modify the code to use logger.DEBUG(bidprice) on the first use to ensure the cron job is properly configured.
