#!/bin/bash

API_KEY=$1
SEVERITY=$2

curl \
 -k "https://api.moogsoft.ai/v1/integrations/events" \
 -H "Content-Type: application/json" \
 -H "apikey: ${API_KEY}" \
 -d '{
    "description": "CPU spike to 75%",
    "severity":  4,
    "source": "www.your-source.com",
    "check": "cpu",
    "service": [
        "retail",
        "support"
    ],
    "tags": {
        "key": "value"
    }
}'
