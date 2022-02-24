#!/usr/bin/python

import json
import os
import queue
import threading
from enum import Enum

import requests
import requests_unixsocket
from thingspro.edge.api_v1 import api
from thingspro.edge.http_v1 import http


class TagType(Enum):
    UINT8  = 1
    UINT16 = 2
    UINT32 = 3
    UINT64 = 4
    INT8   = 5
    INT16  = 6
    INT32  = 7
    INT64  = 8
    FLOAT  = 9
    DOUBLE = 10
    STRING = 11
    BOOLEAN   = 12
    BYTEARRAY = 13
    RAW       = 14

class Token():
    def __init__(self):
        self._ip = os.getenv('APPMAN_HOST_IP', default='localhost')
        self._port = os.getenv('APPMAN_HOST_PORT', default=59000)
        self._prefix = os.getenv('MX_API_VER', default='api/v1/')

        with open("/var/run/mx-api-token") as f:
            token = f.readline()
            self._headers = {"Content-Type": "application/json", "mx-api-token": token.strip()}

class Access(Token):
    """
        Access class provides users to read/write tag directly.
    """

    def __init__(self):
        super().__init__()
        self.__read_tag_url = "http://{}:{}/{}tags/access".format(self._ip, self._port, self._prefix)
        self.__write_tag_url = "http://{}:{}/{}tags/access".format(self._ip, self._port, self._prefix)

    def read(self, provider, source, tag):
        """
            Directly read tag

            :param provider: Provider name
            :param source: Source name
            :param tag: tag name
            :returns status_code: http status code
            :returns message: if status_code is 200 ok, this message will be tag schema as below. otherwise, it’s error message.

                .. code-block::

                    {
                        'prvdName': 'modbus_tcp_master',
                        'srcName': 'ioLogik',
                        'tagName': 'di0',
                        'dataType': 'uint16',
                        'dataValue' 1,
                        'ts': 1607502127595406
                    }
        """
        url = "{}/{}/{}/{}".format(self.__read_tag_url, provider, source, tag)
        r = requests.get(url, headers=self._headers, timeout=3)
        if r.status_code == 200:
            return r.status_code, r.json()
        else:
            return r.status_code, {}

    def _get_data_type(self, data_type_enum):
        #uint8, uint16, uint32, uint64, int8, int16, int32, int64, float, double, string, boolean, byte-array, raw
        if data_type_enum == TagType.UINT8:
            return "uint8"
        elif data_type_enum == TagType.UINT16:
            return "uint16"
        elif data_type_enum == TagType.UINT32:
            return "uint32"
        elif data_type_enum == TagType.UINT64:
            return "uint64"
        elif data_type_enum == TagType.INT8:
            return "int8"
        elif data_type_enum == TagType.INT16:
            return "int16"
        elif data_type_enum == TagType.INT32:
            return "int32"
        elif data_type_enum == TagType.INT64:
            return "int64"
        elif data_type_enum == TagType.FLOAT:
            return "float"
        elif data_type_enum == TagType.DOUBLE:
            return "double"
        elif data_type_enum == TagType.STRING:
            return "string"
        elif data_type_enum == TagType.BOOLEAN:
            return "boolean"
        elif data_type_enum == TagType.BYTEARRAY:
            return "byte-array"
        elif data_type_enum == TagType.RAW:
            return "raw"
        else:
            return "uint16"

    def write(self, provider, source, tag, data_type_enum, data_value):
        """
            Directly write tag

            :param provider: Provider name
            :param source: Source name
            :param tag: tag name
            :param data_type_enum: int8, uint16, uint32, uint64, int8, int16, int32, int64, float, double, string, boolean, byte-array, raw
            :param data_value: According to data_type to assign value
            :returns status_code: http status code
            :returns message: if status_code is 200 ok, this message will be tag schema as below. otherwise error message.

                .. code-block::

                    {
                        'prvdName': 'modbus_tcp_master',
                        'srcName': 'ioLogik',
                        'tagName': 'di0',
                        'dataType': 'uint16',
                        'dataValue' 1,
                        'ts': 1607502127595406
                    }
        """

        url = "{}/{}/{}/{}".format(self.__write_tag_url, provider, source, tag)
        r = requests.put(url, headers=self._headers, json={"dataType": self._get_data_type(data_type_enum), "dataValue": data_value}, timeout=3)
        if r.status_code == 200:
            return r.status_code, r.json()
        else:
            return r.status_code, {}

class Publisher(Token):
    """
        Publisher class provides users to update data by publishing tag.
    """
    def __init__(self):
        super().__init__()
        self._session = requests_unixsocket.Session()
        self.__pub_url = "http+unix://%2Frun%2Ftaghub%2Fhttp.sock/tags/publish"

    def publish(self, data):
        """
            Publish a message on a given tag.

            :param data:

                .. code-block::
                
                    {
                        'prvdName': 'modbus_tcp_master',
                        'srcName': 'ioLogik',
                        'tagName': 'di0',
                        'dataType': 'uint16',
                        'dataValue' 1,
                        'ts': 1607502127595406
                    }
        """
        self._session.post(url=self.__pub_url, data=json.dumps(data))


class Subscriber(Token):
    """
        Publisher class provides users to receive data by subscribing tag.
    """
    def __init__(self):
        super().__init__()
        self._threads = {}
        self._session = requests_unixsocket.Session()
        self.__sub_url = "http+unix://%2Frun%2Ftaghub%2Fhttp.sock/tags/monitor"

    def __has_subscribed(self, provider, source):
        key = "{}/{}".format(provider, source)
        if self._threads.get(key, None) is not None:
            return True, key
        else:
            return False, ""

    def __get_endpoint(self, provider, source, tags):
        sep = ","
        url = "{}/{}/{}?tags={}&onChanged".format(self.__sub_url, provider, source, sep.join(tags))
        return url

    def __tag_monitoring(self, url):
        try:
            r = self._session.get(url=url, headers=self._headers, stream=True)

            if r.encoding is None:
                r.encoding = 'utf-8'

            for line in r.iter_lines(decode_unicode=True):
                if line:
                    data = json.loads(line[5:])
                    if hasattr(self, 'callback'):
                        try:
                            self.callback(data)
                        except Exception as e:
                            print("datadriven callback error({})".format(e))
        except Exception as e:
            print(e)

    def subscribe_callback(self, callback):
        """
            Set the tag subscribe callback.  This is called when the taghub responds to a subscription request.

            :param callback: a handle function to respond to the coming subscription request.

                .. code-block::

                    def callback(data={}):
                        data = {
                            'prvdName': 'modbus_tcp_master',
                            'srcName': 'ioLogik',
                            'tagName': 'di0',
                            'dataType': 'uint16',
                            'dataValue' 1,
                            'ts': 1607502127595406
                        }
        """
        self.callback = callback

    def subscribe(self, provider, source, tags):
        """
            Subscribe to a tag.

            :param provider: Provider name
            :param source: Source name
            :param tags: Array of tags

            Example:

                .. code-block::

                    subscriber.subscribe('modbus_tcp_master', 'Device', ['tag1', 'tag2_t1', 'tag2_t2'])
        """
        if provider == "" or source == "" or not isinstance(tags, list):
            raise ValueError

        if len(tags) == 0:
            raise ValueError

        subscribed, topic = self.__has_subscribed(provider, source)
        if subscribed:
            return

        url = self.__get_endpoint(provider, source, tags)
        self._threads[topic] = threading.Thread(target=self.__tag_monitoring, args=(url, ), daemon=True).start()

    def unsubscribe(self, provider, source):
        if hasattr(self, '_threads'):
            subscribed, topic = self.__has_subscribed(provider, source)
            if not subscribed:
                return

            thread = self._threads.get(topic, None)
            if thread is not None:
                thread.stop()
                self._threads.pop(topic, None)

class DirectAccessTagRegister():
    """
    example:
    {
        "protocolName": "func1_virtual",
        "domainName": "tpfunc", // it's fixed field. DO NOT CHANGED.
        "providers": [
            "func1_virtual"
        ],
        "methods" : {
            "tag-list": "list",
            "direct-read": "direct-read-tag",
            "direct-write": "direct-write-tag"
        }
    }
    """
    def __init__(self, rule_name, provider_name, read_handler=None, write_handler=None):
        self.rule_name = rule_name
        self.read_handler = read_handler
        self.write_handler = write_handler
        data = {}
        data['protocolName'] = rule_name
        data['domainName'] = "tpfunc"
        data['providers'] = [provider_name]
        api_list = {}
        api_list["direct-read"] = f'{rule_name}/direct-read-tag'
        api_list["direct-write"] = f'{rule_name}/direct-write-tag'
        data['methods'] = api_list
        self.registerationJson = json.dumps(data)

    def get_taglist_endpoint(self):
        return f'{self.rule_name}/tag-list'

    def get_direct_read_endpoint(self):
        return f'{self.rule_name}/direct-read-tag'

    def get_direct_write_endpoint(self):
        return f'{self.rule_name}/direct-write-tag'

    def register(self):
        reg_api = api.TPEApiWrapper("post", "tags/prtcl/update")
        r = reg_api.Request(self.registerationJson)
        if r.status_code == 200:
            if self.read_handler is not None:
                http.Server.PUT(f'/{self.rule_name}/direct-read-tag',  self.read_handler)
            if self.write_handler is not None:
                http.Server.PUT(f'/{self.rule_name}/direct-write-tag',  self.write_handler)
            print('direct access tag register succeed. you can use direct access tag api now!')
        else:
            print('direct access tag register fail.')
        return r

    def unregister(self):
        reg_api = api.TPEApiWrapper("delete", "tags/prtcl/update")
        r = reg_api.Request(self.registerationJson)
        if r.status_code == 200:
            print('direct access tag unregister succeed.')
        else:
            print('direct access tag unregister fail.')
        return r
