# ThingsPro Edge Function
## Table of Contents
- [ThingsPro Edge Function](#thingspro-edge-function)
  - [Table of Contents](#table-of-contents)
  - [1. Introduce](#1-introduce)
  - [2. Get Started](#2-get-started)
  - [3. Create your function](#3-create-your-function)
  - [4. Deploy your function](#4-deploy-your-function)
    - [Add function](#add-function)
    - [List function](#list-function)
    - [Delete function](#delete-function)
    - [Start/Stop function](#startstop-function)
  - [5. Debug functions](#5-debug-functions)
  - [6. Types of function](#6-types-of-function)
    - [Type 1. HTTP Server](#type-1-http-server)
    - [Type 2. PubSub tags](#type-2-pubsub-tags)
    - [Type 3: Direct access tag](#type-3-direct-access-tag)
    - [Type 4: Create your own virtual tags](#type-4-create-your-own-virtual-tags)
  - [7. Preview: functions with Data-Driven and Interval Time-Driven Triggers](#7-preview-functions-with-data-driven-and-interval-time-driven-triggers)
    - [Type 5: Detect events/tags and respond](#type-5-detect-eventstags-and-respond)


## 1. Introduce
In ThingsPro Edge, function application provides an easy way to wire togegther your code and the data. Set up the triggers from tags or events and the virtual tags for other applications to re-use easily. No provision and server management are required. Meanwhile, plenties of built-in python library allows you to implement the logic with spectacular ThingsPro features.

## 2. Get Started
To ensure your features work properly, please check the version of AIG or the version of ThingsPro Edge installed in the list below.


| Product | Version | Function version | Python version | API reference |
| ------- | ------- | ---------------- | -------------- | ------------- |
| ThingsPro Edge | 2.3.1 | 1.0.0-275 | [3.5](https://docs.python.org/3.5/library/index.html) | [1.0.0-beta](https://app.swaggerhub.com/apis/CPtung/ThingsProEdgeFunction) |
| AIG-301 | 1.4.0 | 1.0.0-275 | [3.5](https://docs.python.org/3.5/library/index.html) | [1.0.0-beta](https://app.swaggerhub.com/apis/CPtung/ThingsProEdgeFunction) |
| AIG-301 | 1.5.0 | 1.0.0-289 | [3.5](https://docs.python.org/3.5/library/index.html) | [1.0.0](https://tpe-tiger.github.io/AIG301/V1.5/function/#) |
| AIG-301 | 1.6.0 | 1.1.0-517 | [3.9](https://docs.python.org/3.9/library/index.html) | [1.0.0](https://tpe-tiger.github.io/AIG301/V1.6/function/#) |
| AIG-501 | 1.2.0 | 1.0.0-275 | [3.5](https://docs.python.org/3.5/library/index.html) | [1.0.0-beta](https://app.swaggerhub.com/apis/CPtung/ThingsProEdgeFunction) |
| AIG-501 | 1.3.0 | 1.0.0-317 | [3.5](https://docs.python.org/3.5/library/index.html) | [1.0.0](https://tpe-tiger.github.io/AIG501/V1.3.0/function/#) |
| AIG-501 | 1.4.0 | 1.1.0-517 | [3.9](https://docs.python.org/3.9/library/index.html) | [1.0.0](https://tpe-tiger.github.io/AIG501/V1.4.0/function/#) |
| AIG-302 | 1.0.0 | 0.3.4+6841 | [3.9](https://docs.python.org/3.9/library/index.html) | [1.0.0](https://tpe-tiger.github.io/AIG302/V1.0.0/#tag/function) |

- Since the function runtime is built based on **Python**, you can also refer to Python official library for implementation.


## 3. Create your function

To start the very first step, you can download the examples [here](./examples/). Take [demo](./examples/demo/) for example.

>We also provide a experimental built-in utility `tpfunc` which can help you start with a template `index.py` and `pacakge.json`.
>This utility supports the following products:
>| Product | Version |
>| ------- | ------- |
>| AIG-301 | 1.4, 1.5 |
>| AIG-501 | 1.2+ |
>You can refer [this document](./tpfunc.md) to try this utility.


```bash
./demo
 +- index.py      # main source file for your function code
 +- package.json  # describes properties for your function
```
#### package.json
```json
{
  "name": "demo",
  "enabled": true,
  "trigger": {
    "driven": "timeDriven",         // ["dataDriven", "timeDriven"]
    "dataDriven": {
      "tags": {},
      "events": {}
    },
    "timeDriven": {
      "mode": "boot",               // ["boot", "interval", "cronJob"]
      "intervalSec": 1,
      "cronJob": ""
    }
  },
  "expose": {
    "tags": []
  },
  "params": {
    "version": "1.0"
  }
}
```
>You can find the specification of `package.json` [here](./package.json.md).


#### index.py
```python
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
```

This sample will print all parameters listed in `params` objects defined in `package.json`.


## 4. Deploy your function
Now your first function has been created, then we can move on to how to deploy it. There are 2 methods to deploy your function, We will explain how to do both.
1. Import the function via Web
2. Add the function by REST API


### Add function
First to compress your program directory into a tar.gz file. For example, compress the demo sample to demo.tar.gz.

#### Via Web Interface
1. Navigate to Edge Computing > Function Management
2. Click Import function and Browse your function file, click Upload.

#### Via REST API
* API Endpoint: `POST /api/v1/function`
* Command Example:
  ```bash
  curl --location --insecure --request POST \
      --form 'file=@<file-path>' \
      --header 'Content-Type: multipart/form-data' \
      --header 'Authorization: Bearer <token>' \
      'https://<device-ip>:8443/api/v1/function'
  ```

Unless the files under your function directory are missing or the format is incorrect, adding function is always successful.\
The next section will show you how to check your function is deployed and running properly.

### List function

#### Via Web Interface
After added the function, you'll find it's current status in the list.

#### Via REST API
* API Endpoint: `GET /api/v1/function`
* Command Example:
  ```bash
  curl --location --insecure --request GET \
      --header 'Authorization: Bearer <token>' \
      'https://<device-ip>:8443/api/v1/function'
  ```
* The response is a json `data` array that include the whole `package.json` and runtime `executable` object.
  ```json
  {
    "data": [
      {
        "id": 1,
        "name": "demo",
        "enabled": true,
        "trigger": {
          "driven": "timeDriven",
          "dataDriven": {
            "tags": {},
            "events": {}
          },
          "timeDriven": {
            "mode": "boot",
            "cronJob": "",
            "intervalSec": 1
          }
        },
        "expose": {
          "tags": []
        },
        "executable": {
          "language": "python",
          "context": "<index.py>",
          "lastUpTime": "2025-01-20T16:45:43+08:00",
          "state": "running",
          "error": ""
        },
        "params": {
          "version": "1.0"
        }
      }
    ]
  }
  ```
  * `executable.context`: Contain the whole `index.py`.
  * `executable.lastUpTime`: The last up time of the function.
  * `executable.state`: Current state of the function.
  * `executable.error`: Shows the error reason when the function crashed.

### Delete function

#### Via Web Interface
1. Locate the function you want to delete.
2. Click the three dots (⋮) on the right side of the desired item.
3. Select Delete from the dropdown menu to confirm and complete the deletion.

#### Via REST API
* API Endpoint: `DELETE /api/v1/function?id=<function-name>`
* Command Example:
  ```bash
  curl --location --insecure --request DELETE \
      --header 'Authorization: Bearer <token>' \
      'https://<device-ip>:8443/api/v1/function?id=<function-name>'
  ```


### Start/Stop function

#### Via Web Interface
1. Locate the function you want to delete.
2. Click the three dots (⋮) on the right side of the desired item.
3. Select Enable or Disable from the dropdown menu to start or stop the function.

#### Via REST API
* API Endpoint: `PATCH /api/v1/function`
* Request Body Example:
  ```json
  {
    "name": "<function-name>",
    "enabled": <true|false>
  }
  ```
* Command Example:
  ```bash
  curl --location --insecure --request PATCH \
      --header 'Authorization: Bearer <token>' \
      --data '{"name": "<function-name>", "enabled": <true|false>}' \
      'https://<device-ip>:8443/api/v1/function'
  ```


## 5. Debug functions
During the development and deployment, there always needs a way to the debug.
In ThingsPro Edge Function, a real-time logging channel setup by default when each funciton starts.
As long as user hit the log API, the streaming `stdout` and `stderr` will be printed on screen by time sequence.

* API Endpoint: `GET /api/v1/function/log?id=<function-name>&event`
* Command Example:
  ```bash
  curl --insecure --include --no-buffer --output - --request GET \
        --header 'Authorization: Bearer <token>' \
        --header "Content-Type: application/json" \
        'https://${URL}:8443/api/v1/function/log?id=<function-name>&event'
  ```


## 6. Types of function


### Type 1. HTTP Server
Some use cases will require accessing the function via an HTTP(s) request. By ThingsPro Edge Function, you can invoke those APIs with an HTTP request using the POST, PUT, GET and DELETE without implement a server, even a ThingsPro application. First, download the function [http](./examples/http/). Since the API function doesn't have to start repeatly or restart refrequently, `package.json` has been configured as boot mode.

> * Concurrent requests in a REST API is not handled.
> * The API authentication is still required, so ensure you have the token before applying the APIs. Besides, a hard prefix `api/v1/tpfunc/` is always ahead of all HTTP function endpoints. The whole path will looks like `https://{IP}/api/v1/tpfunc/{PATH}`.

This example display a dummy Get method `world/hello` always return `Hello World` message.

#### package.json
```json
{
  "name": "http",
  "enabled": true,
  "trigger": {
    "driven": "timeDriven",
    "dataDriven": {
      "tags": {},
      "events": {}
    },
    "timeDriven": {
      "mode": "boot",
      "intervalSec": 1,
      "cronJob": ""
    }
  },
  "expose": {
    "tags": []
  },
  "params": {}
}
```

#### index.py
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import json
from thingspro.edge.http_v1 import http


def hello_world(resource, headers, message):
    """ GET method by callback function """
    return http.Response(code=200, data="Hello World")

if __name__ == "__main__":
    # callback function
    http.Server.GET("/world/hello", hello_world)
    # infinite loop
    while True:
        time.sleep(1)
```

### Type 2. PubSub tags

Although we already have provide data trigger callback function, sometimes user prefer handle the function lifecycle on their own. To get the tag without data callback, PubSub pattern is also available in ThingsPro Edge function. In this example, we are going to subscribe a few of tags and scaling the value, then publish them to become a new virtual tag.

First, we define this function is triggered by boot time. Meanwhile, it is also the provider of the virtual tag `modbus_tcp_master/device/di0_scale` that defined in `expose` section.

#### package.json
```json
{
  "name": "scale",
  "enabled": true,
  "trigger": {
    "driven": "timeDriven",
    "dataDriven": {
      "tags": {},
      "events": {}
    },
    "timeDriven": {
      "mode": "boot",
      "intervalSec": 1,
      "cronJob": ""
    }
  },
  "expose": {
    "tags": [
      {
        "prvdName": "modbus_tcp_master",
        "srcName": "device",
        "tagName": "di0_scale",
        "dataType": "double"
      }
    ]
  },
  "params": {}
}
```
Then, we look into `index.py`. As long as the subscribed Modbus tag is coming, the value will be scaled by the formula `scale_value=value*factor-offset` and re-published as the virtual tag.

#### index.py
```python
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
    # publish the scaling data as the defined virtual tag
    publisher.publish(data)

if __name__ == "__main__":
    # create subscriber client instance
    subscriber = tag.Subscriber()
    subscriber.subscribe_callback(callback)
    subscriber.subscribe('modbus_tcp_master', 'Demo', ['tag1', 'tag2_t1', 'tag2_t2'])
    # create publisher client instance
    publisher = tag.Publisher()
    # infinite loop
    while True:
        time.sleep(1)
```

#### Where can find the new virtual tag?
If you already had cloud connectivity in ThingsPro Edge, such as **Azure IoT Edge/Device**, even **generic MQTT**.Now you can open the tag select page, the virtual tag should be listed under the provider name you defined in package.json.

### Type 3: Direct access tag

Although we already have subscribed tag, sometimes user prefer on-demand access read or write tag directly. To get the tag without subcription routine, Access pattern is also available in ThingsPro Edge function. In this example, we are going to directly read and write tag.

Note: Direct access doesn't support system tag.

First, we define this function is triggered by boot time.
#### package.json
```json
{
  "name": "access",
  "enabled": true,
  "trigger": {
    "driven": "timeDriven",
    "dataDriven": {
      "tags": {},
      "events": {}
    },
    "timeDriven": {
      "mode": "boot",
      "intervalSec": 1,
      "cronJob": ""
    }
  },
  "expose": {
    "tags": []
  },
  "params": {}
}
```
Then, we look into `index.py`. Accesser Read Tag API need provider name, source name, and tag name parameters, then get result from  `dataValue` and `dataType` fields of responsed json data. Similarly, Accesser Write Tag API need extra `dataValue` and `dataType` fields. Please be noticed that `dataType` is enum type of `thingspro.edge.tag_v1` library.

#### index.py
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
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

```


### Type 4: Create your own virtual tags


User can self-defined virtual tags in function rule program, and these tags will be auto-generated into Thingspro Edge Tag Service. Thus, we're able to operate these virtual tags by `Taghub` api. e.g. `tags/list`.
Additionally, function progrom SDK also provide simple way let programer to register direct access method of the defined virtual tags. Follow below steps, user can use `tags/access/${ProviderName}/${SourceName}/${TagName}`
to access registered callback function to do read or write operation.

First, we define this function is triggered by boot time.
#### package.json
```json
{
  "name": "vtag_access_func1",
  "enabled": true,
  "trigger": {
    "driven": "timeDriven",
    "dataDriven": {
      "tags": {},
      "events": {}
    },
    "timeDriven": {
      "mode": "boot",
      "cronJob": ""
    }
  },
  "expose": {
    "tags": [
      {
      "prvdName": "vtag_access_func1",
      "srcName": "cpu",
      "tagName": "onchange",
      "dataType": "double",
      "access": "rw"
      }
    ]
  },
  "params": {}
}
```
Then, we look into `index.py`. Direct Access Tag Register API need rule name, provider name, and your defined callback handler. Remember to do `unregister()` before your python program exit.

#### index.py
```python
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

```

## 7. Preview: functions with Data-Driven and Interval Time-Driven Triggers

There are some preview trigger modes, such as those activated by data-driven events or internal timing. These modes can be utilized during development or testing.


#### package.json
```json
{
  "name": "demo",
  "enabled": true,
  "trigger": {
    "driven": "dataDriven",         // ["dataDriven", "timeDriven"]
    "dataDriven": {
      "tags": {},
      "events": {}
    },
    "timeDriven": {
      "mode": "interval",               // ["boot", "interval", "cronJob"]
      "intervalSec": 1,
      "cronJob": ""
    }
  },
  "expose": {
    "tags": []
  },
  "params": {
    "version": "1.0"
  }
}
```


### Type 5: Detect events/tags and respond
Once you create the function with `--trigger-data`, you can add those tags and events that you want to detect and respond. This example will listen to a tag `/system/status/cpuUsage` and a event `system/app stop`.

#### package.json
```json
{
  "name":"demo",
  "enabled":true,
  "trigger":{
    "driven":"dataDriven",
    "dataDriven":{
      "tags":{
        "system": {
          "status": [
            "cpuUsage"
          ]
        }
      },
      "events":{
        "system": [
          "app stop"
        ]
      }
    },
    "timeDriven":{
      "mode":"boot",
      "intervalSec":1,
      "cronJob":""
    }
  },
  "expose":{},
  "executable": {
    "language": "python"
  },
  "params":{}
}
```

After tag and event are added to the configuration. Looking to `index.py`, you should see the below template has been created. As shown, you can tell the incoming data is tag or event by the parameter `_type`. To be friendly, the structure of event and tag are attached in the comment session in advanced. Reminder, this example doesn't complete the code, so before the deployment, you have to fill the rest of the data callback function otherwise you will get yourself the error messages for python syntax error.

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ThingsPro Edge Function data driven function template
"""

# When using the data-driven pattern, the callback function name YOUR_DATA_CALLBACK must match your function name. Please avoid using names that are against python's rule of function names, such as reserved keywords or operators.
def YOUR_DATA_CALLBACK(_type, data):
    """Two types of data will be passed into
        your callback funciton - [tag, event].
        You can tell each other by the _type flag.

    :param tag: A dict mapping keys to the corresponding structure of tag.
                example:
                {
                'prvdName': 'modbus_tcp_master',
                'srcName': 'ioLogik',
                'tagName': 'di0',
                'dataType': 'uint16',
                'dataValue' 1,
                'ts': 1607502127595406
                }

    :param event: A dict mapping keys to the corresponding structure of event.
                example:
                {
                'createdAt': '2020-12-09T17:44:01.271483145+08:00',
                'event': 'app start',
                'category': 'system',
                'user': '',
                'userOrigin': '',
                'id': 0,
                'message': 'Application started: Modbus Master',
                'severity': 'info',
                'origin': 'system'
                }
    """
    if _type == 'tag':
        # TODO: tag handler

    elif _type == 'event':
        # TODO: event handler

```

AIG-301/501 Series support more than 60+ events, refer to <a href="https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/TPE2-EventList.md">the link</a> for detail.

>!! `dataDriven.events` is not currently supported for AIG-302 Series due to a known issue. Future updates may address this limitation.