#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json


class Configuration():
    """
    Configuration class provides the properties value in package.json
    """
    def __init__(self):
        self.__load_configuration()
        self.__load_trigger_time()

    def __load_configuration(self):
        try:
            cwd = os.getcwd()
            config = os.getenv('CONFIG')
            config = (cwd + '/package.json') if config is None else config
            with open(config, "r") as f:
                self._db  = json.load(f)
        except Exception as e:
            self.__load_default()

    def __load_default(self):
        self._db = {}
        self._db['executable'] = {}
        self._db['trigger'] = {}
        self._db['expose'] = {}
        self._db['params'] = {}

    def __load_trigger_time(self):
        data = os.getenv('DATA')
        self.__trigger_time = data if data else ""

    def data_driven_tags(self):
        """
        Return the value of key **tags** in package.json.

        :Example:
            .. code-block:: python
            
                {
                    "system": {
                        "status": [
                            "cpuUsage"
                        ]
                    }
                }
        """
        trigger = self._db['trigger'].get('dataDriven', None)
        if trigger is None:
            return {}
        return trigger.get('tags', {})

    def data_driven_events(self):
        """
        Return the value of key **events** in package.json.

        :Example:
            .. code-block:: python
            
                {
                    "system": {
                        "status": [
                            "cpuUsage"
                        ]
                    }
                }

        """
        trigger = self._db['trigger'].get('dataDriven', None)
        if trigger is None:
            return {}
        return trigger.get('events', {})

    def name(self):
        """
        Return the name of your function package.

        :Example: {YOUR FUNCTION NAME}
        """
        return self._db.get('name', '')

    def expose_tags(self):
        """
        Return the value of key **expose** in package.json.

        :Example:
            .. code-block::

                [
                    {
                        "prvdName": "user",
                        "srcName": "define",
                        "tagName": "tag",
                        "dataType": "double",
                        "access": "r"
                    }
                ]
        """
        return self._db['expose'].get('tags', [])

    def parameters(self):
        """
        Return pre-defined parameters.

        :Example:
            .. code-block:: python
            
                {
                    'version': '1.0.0',
                    'arch': 'amd64'
                }

        """
        return self._db.get('params', {})

    def boot_time(self):
        """
        The start time of your function.
        
        :Example: string in ISO-8601 date format
        """
        return self.__trigger_time
