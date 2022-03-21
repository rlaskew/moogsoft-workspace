#!/usr/bin/env python3

import json
import requests
import sys
import getopt 
import moogsoft

print (sys.argv[0],sys.argv[1])

api_key = sys.argv[1]
severity = int(sys.argv[2])

# Set the webhook_url
webhook_url = 'https://api.moogsoft.ai/v1/integrations/events'
moogsoft_data = {
    "description": "CPU spike to 75%",
    "severity":  severity,
    "source": "www.your-source.com",
    "check": "cpu",
    "service": [
        "retail",
        "support"
    ],
    "tags": {
        "key": "value"
    }
}

response = requests.post(
    webhook_url, data=json.dumps(moogsoft_data),
    headers={'Content-Type': 'application/json', 'apikey': api_key}
)

print (response.status_code, response.text, api_key, severity)

#if response.status_code != 200:
#    raise ValueError(
#        'Request to moogsoft returned an error %s, the response is:\n%s'
#        % (response.status_code, response.text)
#    )
