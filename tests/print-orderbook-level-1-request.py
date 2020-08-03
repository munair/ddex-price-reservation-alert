#!/usr/bin/env python3

import json
from urllib.request import Request, urlopen

# define request
request = Request('https://api.ddex.io/v4/markets/ETH-USDC/orderbook?level=1', headers={'User-Agent': 'Mozilla/5.0'})

# get content and its encoding
content = urlopen(request).read()
encoding = urlopen(request).info().get_content_charset('utf-8')

# process content
dictionary = json.loads(content.decode(encoding))
jsondata = json.dumps( dictionary, sort_keys=True, indent=4, separators=(',', ': ') )

# print content
print ( jsondata )
