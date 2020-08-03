#!/usr/bin/env python3
# Note: run as a cron job

# standard
import time
import json
from decimal import Decimal
from urllib.request import Request, urlopen

# custom
from libraries.logger import logger
from libraries.messenger import smsalert

# set price alert
# NOTE: DDEX limits API requests to 30 per minute per IP
reservationprice = 398.95
# GOING LONG?
# Then sell when buyers are meeting/exceeding this reservation price.

# define request
request = Request('https://api.ddex.io/v4/markets/ETH-USDC/orderbook?level=1', headers={'User-Agent': 'Mozilla/5.0'})

# get content and its encoding
content = urlopen(request).read()
encoding = urlopen(request).info().get_content_charset('utf-8')

# process content
dictionary = json.loads(content.decode(encoding))
bidprice = dictionary["data"]["orderbook"]["bids"][0]["price"]
if Decimal(bidprice) > reservationprice:
    # send alert to mobile phone
    smsalert(f'the last bid [{bidprice} USDC] for ETH exceeded {reservationprice} USDC')

# Runtime on MacBook Pro:
# real	0m1.144s
# user	0m0.305s
# sys	0m0.085s
