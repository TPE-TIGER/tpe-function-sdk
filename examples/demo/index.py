#!/usr/bin/python
# -*- coding: utf-8 -*-

from thingspro.edge.func_v1 import package


if __name__ == "__main__":
    # create function client instance
    config = package.Configuration()
    # print parameters defined inpackage.json
    print(config.parameters())

    # infinite loop
    while True:
        time.sleep(1)