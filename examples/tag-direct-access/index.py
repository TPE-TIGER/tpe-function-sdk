#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import signal
import sys
import time

from thingspro.edge.api_v1 import api
from thingspro.edge.http_v1 import http
from thingspro.edge.tag_v1 import tag as tpeTAG

tag_value = 0.0

def signal_handler(sig, frame):
    print('function rule exit, unregister direct access tag callback')
    global direct_access_register
    direct_access_register.unregister()
    sys.exit(0)

def read_tag(resource, headers, message):
    print("Implement your direct read virtual tag here!")
    tag = {
        'prvdName': "vtag_access_func1",
         'srcName': "cpu",
        'tagName': "onchange",
        'dataValue': tag_value,
        'dataType' : "double",
         'ts': 0
    }
    return http.Response(code=200, data=tag)

def write_tag(resource, headers, message):
    '''
    e.g.
        message:{dataType: double,dataValue: 1}
    '''

    print("Implement your direct write virtual tag here!")

    json_payload = json.loads(message)
    tag = {
        'prvdName': "vtag_access_func1",
         'srcName': "cpu",
        'tagName': "onchange",
        'dataValue': float(json_payload["dataValue"]),
        'dataType' : "double",
         'ts': 0
    }
    print(tag)
    global tag_value
    tag_value = float(json_payload["dataValue"])
    global publisher
    publisher.publish(tag)
    return http.Response(code=200, data=tag)

if __name__ == "__main__":

    publisher = tpeTAG.Publisher()

    direct_access_register = tpeTAG.DirectAccessTagRegister("vtag_access_func1", "vtag_access_func1", read_handler=read_tag, write_handler=write_tag)
    direct_access_register.register()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # infinite loop
    while True:
        if tag_value == 100:
            tag_value = 0
        tag = {
                'prvdName': "vtag_access_func1",
                'srcName': "cpu",
                'tagName': "onchange",
                'dataValue': tag_value,
                'dataType' : "double",
                'ts': 0
        }
        print(tag)
        publisher.publish(tag)
        tag_value = tag_value + 1
        time.sleep(5)
