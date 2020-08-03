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
        askprice = dictionary["data"]["orderbook"]["asks"][0]["price"]
        if Decimal(askprice) > reservationprice:
            time.sleep(5) # DDEX limits API requests to 30 per minute per IP
        else:
            smsalert(f'the last ask [{askprice} USDC] for ETH fell below {reservationprice} USDC') # send alert to mobile phone
            break # exit loop

if __name__ == "__main__":
    # set price alert
    reservationprice = 398.95
    # GOING LONG?
    # Then buy when sellers are dumping ETH at prices below this reservation price.
    try:
        # poll DDEX servers
        poller( reservationprice )
    except KeyboardInterrupt:
        logger.debug( f'exception: keyboard interuption.' )
    except Exception as e:
        logger.debug( f'exception: {e}.' )
    logger.debug( f'exiting...' )
    exit(0)
    # Loop runtime on MacBook Pro:
    # real	0m3.205s
    # user	0m0.393s
    # sys	0m0.105s
