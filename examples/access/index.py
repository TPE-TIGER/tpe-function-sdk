#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time

from thingspro.edge.tag_v1 import tag

if __name__ == "__main__":
    # create accesser client instance
    accesser = tag.Access()

    # provider name, source name, and tag name
    resp = accesser.read("modbus_tcp_master", "Demo", "di0")
    print(resp)

    # provider name, source name, tag name, data type, data value
    resp = accesser.write("modbus_tcp_master", "Demo", "di1", tag.TagType.INT16, random.randint(0,99))
    print(resp)

    while True:
        time.sleep(1)
