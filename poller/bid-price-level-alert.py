#!/usr/bin/env python3

# standard
import time
import json
from decimal import Decimal
from urllib.request import Request, urlopen

# custom
from libraries.logger import logger
from libraries.messenger import smsalert

def poller( reservationprice: float ) -> None:
    # define request
    request = Request('https://api.ddex.io/v4/markets/ETH-USDC/orderbook?level=1', headers={'User-Agent': 'Mozilla/5.0'})

    # get content and its encoding
    content = urlopen(request).read()
    encoding = urlopen(request).info().get_content_charset('utf-8')
    while True:
        # process content
        dictionary = json.loads(content.decode(encoding))
        bidprice = dictionary["data"]["orderbook"]["bids"][0]["price"]
        if Decimal(bidprice) < reservationprice:
            time.sleep(2) # DDEX limits API requests to 30 per minute per IP
        else:
            smsalert(f'bids for ETH exceed {reservationprice} USDC') # send alert to mobile phone
            break # exit loop

            # Loop runtime on MacBook Pro:
            # real	0m3.205s
            # user	0m0.393s
            # sys	0m0.105s

if __name__ == "__main__":
    # set price alert
    reservationprice = 398.95
    # IF LONG: sell when buyers are meeting/exceeding the reservation price
    # OTHERWISE: buy when buyers are meeting/exceeding the reservation price
    try:
        # poll DDEX servers
        poller( reservationprice )
    except KeyboardInterrupt:
        logger.debug( f'exception: keyboard interuption.' )
    except Exception as e:
        logger.debug( f'exception: {e}.' )
    logger.debug( f'exiting...' )
    exit(0)
