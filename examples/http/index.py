#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import json

from thingspro.edge.http_v1 import http
from thingspro.edge.http_v1.http import http_get

@http_get(resource="/world/hello")
def hello_world(resource, headers, message):
    """ Example for get method by decorator """
    return http.Response(code=200, data="Hello!")

def change_world(resource, headers, message):
    """ Example for put method by callback function """
    data={"message":"world is fine, nothing to change"}
    return http.Response(code=400, data=data)


if __name__ == "__main__":
    # decorator
    hello_world()
    # callback function
    http.Server.PUT('/world/change', change_world)
    # infinite loop
    while True:
        time.sleep(1)
