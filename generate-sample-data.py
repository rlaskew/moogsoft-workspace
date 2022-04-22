#!/usr/bin/env python3

## args choices https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/

import json
import requests
import sys
import getopt 
import moogsoft
import time

def post_to_events_api(event_webhook_url, json_data, moogsoft_api_key):
  response = requests.post(
      event_webhook_url, data=json.dumps(json_data),
      headers={'Content-Type': 'application/json', 'apikey': moogsoft_api_key}
  )
  return (response.status_code, response.text)

print (sys.argv[0], sys.argv[1])

api_key = sys.argv[1]

## read config settigns
set_description = moogsoft.myhost["set_description"]
set_severity = moogsoft.myhost["set_severity"]
clear_severity = moogsoft.myhost["clear_severity"]
demo_namespace = moogsoft.config_data["demo_namespace"]
set_iterations = moogsoft.myhost["set_iterations"]
set_duration = moogsoft.myhost["set_duration"]

# Set the webhook_url
webhook_url = 'https://api.moogsoft.ai/v1/integrations/events'
moogsoft_data = {
    "description": set_description,
    "severity":  set_severity,
    "source": "www.your-source.com",
    "check": "cpu",
    "namespace": demo_namespace,
    "service": [
        "retail",
        "support"
    ],
    "tags": {
        "key": "value",
        "location_code": "TXPLANB1F1"
    }
}

for i in range(1,set_iterations):
    #print (str(i))
    (rStatus, rText) = post_to_events_api( webhook_url,
                       moogsoft_data,
                      api_key)
    print (rStatus, rText, api_key, set_description, moogsoft_data["severity"])
    time.sleep(set_duration)

time.sleep(3)
moogsoft_data["severity"] = clear_severity 
(rStatus, rText) = post_to_events_api( webhook_url,
                    moogsoft_data,
                    api_key)

print (rStatus, rText, api_key, set_description, moogsoft_data["severity"])

#if response.status_code != 200:
#    raise ValueError(
#        'Request to moogsoft returned an error %s, the response is:\n%s'
#        % (response.status_code, response.text)
#    )
