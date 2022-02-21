#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from thingspro.edge.tag_v1 import tag


def scale_value(val, factor, offset):
    """ Scaling Value """
    # scale formula
    scale = (val * factor) - offset
    
    # max/min value if-else statements
    if scale > 32767:
        return 32767
    elif scale < 0:
        return 0
    else:
        return scale


def callback(data={}):
    global publisher
    data['dataValue'] = scale_value(data['dataValue'], 1000, 31268)
    if data['tagName'] == 'tag1':
        data['tagName'] = 'di0_scale'
    else:
        data['tagName'] = 'di1_scale'
    publisher.publish(data)


if __name__ == "__main__":
    # create subscriber client instance
    subscriber = tag.Subscriber()
    subscriber.subscribe_callback(callback)
    subscriber.subscribe('modbus_tcp_master', 'Demo', ['tag1', 'tag2_t1', 'tag2_t2'])
    
    # create publisher client instance
    publisher = tag.Publisher()

    while True:
        time.sleep(1)

