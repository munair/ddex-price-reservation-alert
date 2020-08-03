# Server Preparation

To begin, fire up an EC2 instance running Ubuntu 18.04.4 LTS (GNU/Linux 5.3.0-1023-aws x86_64) from your AWS Console. Then go ahead and ssh in to your instance with a command that looks something like:

```bash
ssh -i ~/.ssh/usefulcoin.pem -l ubuntu 102.35.93.131
```

# Installing Dependencies

This solution is all about messaging and we are going to be using Boto3 from AWS to send messages. This dependency must be installed:

```bash
sudo apt update # update apt
python3 --version # confirm that python3 is installed (it is by default on Ubuntu Server 18.04 LTS)
pip3 --version || sudo apt install python3-pip -y # check for pip3 and install it if not found
pip3 install boto3 # install boto3 libraries at long last
```

# Setup Guide

The remaining steps should be customized to your suit. Of course, the AWS stuff must be configured with your credentials. Once that's done, clone the repository, select your poller (either ask or bid) from the poller directory, and set your reservation price. Any remaining steps are totally optional.

## Steps

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

4. Download the repository, make it the present working directory, and choose your poller:

```bash
git config --global user.email "incrementalcapital@gmail.com" # optional
git config --global user.name "incremental capital" # optional
git clone https://github.com/munair/ddex-price-reservation-alert.git
cd ddex-price-reservation-alert
cp poller/bid-reservation-price-level-alert.py poller.py
```

5. Set the reservation price:

```bash
sed -i "s/reservationprice =.*/reservationprice = 382.15/" poller.py
```

6. Run the following command to start the poller:

```bash
nohup /usr/bin/python3 /home/ubuntu/ddex-price-reservation-alert/poller.py &
```

7. Check the /tmp/poller.err log file for errors and ensure the script job is properly detached:

```bash
tail -f /tmp/poller.err
```

## Additional Configuration

1. In case you need to dig into the logs, set up your timezone:

```bash
sudo timedatectl set-timezone America/Mexico_City
```

This configures the instance timezone to ensure that the date and time are properly recorded.

2. Run monitor.bash to get an alert the minute the poller process dies:

```bash
bash monitor.bash
```
