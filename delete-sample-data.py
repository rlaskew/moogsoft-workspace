#!/usr/bin/env python3

# from https://api.docs.moogsoft.com/reference/search
import json
import requests
import sys
import getopt 
import moogsoft

print (sys.argv[0], sys.argv[1])

api_key = sys.argv[1]

## read config settigns
set_description = moogsoft.myhost["set_description"]
demo_namespace = moogsoft.config_data["demo_namespace"]

# Set the webhook_url
#webhook_url = 'https://api.moogsoft.ai/v1/alerts-search' + '?namespace=moogsoft-demo'
webhook_url = 'https://api.moogsoft.ai/v1/alerts-search' + '?namespace=' + demo_namespace
moogsoft_data = {
    "search.namespace": "moogsoft-demo"
}

response = requests.get(
    webhook_url, data=json.dumps(moogsoft_data),
    headers={'Content-Type': 'application/json', 'apikey': api_key}
)

print (response.status_code, 
	response.text, 
	api_key, 
	set_description)

response_json = json.loads(response.text)
alerts_to_delete = response_json["data"]
for x in alerts_to_delete:
  print (x)

#if response.status_code != 200:
#    raise ValueError(
#        'Request to moogsoft returned an error %s, the response is:\n%s'
#        % (response.status_code, response.text)
#    )
