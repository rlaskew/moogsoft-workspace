#!/usr/bin/env python3

# from https://martin-thoma.com/configuration-files-in-python/
import preprocessing

config_data = { 
     "demo_namespace": "moogsoft_demo"
}

myhost = {
   "hostname": "txplanserver1"
   ,"set_duration": 150
   ,"set_severity": 5
   ,"set_description": "txplanserver1 is down"
   ,"clear_duration": 30
   ,"clear_severity": 0
}
