#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import json
import signal
import sys
import time

from thingspro.edge.api_v1 import api
from thingspro.edge.http_v1 import http
from thingspro.edge.tag_v1 import tag


def signal_handler(sig, frame):
    print('function rule exit, unregister direct access tag callback')
    global direct_access_register
    direct_access_register.unregister()
    sys.exit(0)

def read_tag(resource, headers, message):
    data={"message": "Implement direct read virtual tag here!"}
    return http.Response(code=200, data=data)


def write_tag(resource, headers, message):
    data={"message": "Implement direct write virtual tag here!"}
    return http.Response(code=200, data=data)

def tag_list(resource, headers, message):
    data={"message": "Implement self virtual tag list here!"}
    return http.Response(code=200, data=data)

if __name__ == "__main__":

    direct_access_register = tag.DirectAccessTagRegister("vtag_access_func1", "vtag_access_func1", taglist_handler=tag_list, read_handler=read_tag, write_handler=write_tag)
    direct_access_register.register()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # infinite loop
    while True:
        time.sleep(1)
