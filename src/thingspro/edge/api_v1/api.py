#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import os
import threading
import time

import requests


class Token():
    def __init__(self):
        self._ip = os.getenv('APPMAN_HOST_IP', default='localhost')
        self._port = os.getenv('APPMAN_HOST_PORT', default=59000)
        self._prefix = os.getenv('MX_API_VER', default='api/v1/')

        with open("/var/run/mx-api-token") as f:
            token = f.readline()
            self._headers = {"Content-Type": "application/json", "mx-api-token": token.strip()}


class TPEApiWrapper(Token):
    def __init__(self, method, path):
        super().__init__()

        if not self.__check_valid_http_method(method.upper()):
            raise Exception(f"invalid http method: {method}")
        if len(path) == 0:
            raise Exception(f"invalid http path: {path}")
    
        self.method = method.upper()
        self.path = path
  
    def __check_valid_http_method(self, method):
        if method != "GET" and method != "PUT" and method != "POST" and method != "DELETE":
            return False
        else: 
            return True

    def __call__(self, f):
        def wrapper(obj, *args, **kwargs):
            payload = f(*args, **kwargs)
            args = {
                'method': self.method,
                'url': 'http://{}:{}/{}{}'.format(self._ip, self._port, self._prefix, self.path),
                'headers': self._headers,
            }
            if payload is not None:
                args['data'] = payload
  
            r = requests.request(**args)
            return r
        return wrapper

    def Request(self, payload):
        args = {
            'method': self.method,
            'url': 'http://{}:{}/{}{}'.format(self._ip, self._port, self._prefix, self.path),
            'headers': self._headers,
        }
        if payload is not None:
            args['data'] = payload

        r = requests.request(**args)
        return r
