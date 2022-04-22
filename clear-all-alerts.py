#!/usr/bin/env python3

## args choices https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

import json
import requests
import sys
import getopt 
import moogsoft

def set_alert_to_closed(alerts_webhook_url, moogsoft_api_key):
  payload = {"status":"closed"}
  response = requests.patch(
      alerts_webhook_url,
      json=payload,
      headers={'Content-Type': 'application/json', 'apikey': moogsoft_api_key}
  )
  return (response.status_code, response.text)

def get_all_alerts_api(alerts_webhook_url, moogsoft_api_key):
  response = requests.get(
      alerts_webhook_url,
      headers={'Content-Type': 'application/json', 'apikey': moogsoft_api_key}
  )
  return (response.status_code, response.text)

print (sys.argv[0], sys.argv[1])

api_key = sys.argv[1]

# Set the webhook_url
webhook_url = 'https://api.moogsoft.ai/v1/alerts?limit=1'

(rStatus, rText) = get_all_alerts_api( webhook_url,
                    api_key)

#print (rStatus, rText, api_key)

d = json.loads(rText)

for i in d["data"]["result"]:
    print ("Row:",i["alert_id"])
    webhook_url = 'https://api.moogsoft.ai/v1/alerts/' + str(i["alert_id"])
    print (webhook_url)
    (rStatus, rText) = set_alert_to_closed(webhook_url, api_key)
    print (rStatus, rText, api_key)
