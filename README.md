# ThingsPro Edge Function
## 1. Introduce
In ThingsPro Edge, function application provides an easy way to wire togegther your code and the data. Set up the triggers from tags or events and the virtual tags for other applications to re-use easily. No provision and server management are required. Meanwhile, plenties of built-in python library allows you to implement the logic with spectacular ThingsPro features.
## 2. Get Started
To be sure your functions can run properly. Please check the unit has installed the latest **ThingsPro Edge v2.2**.

**ThingsPro Edge function:**
- [Source code](https://github.com/MOXA-ISD/edge-thingspro-function)
- [API reference](https://app.swaggerhub.com/apis/CPtung/ThingsProEdgeFunction)
- [Module reference](http://s3.moxa.online/v3/edge/builds/edge-thingspro-function/master/latest)
- Since the function runtime is built on **Python 3.5**, you can also refer to [Python official library](https://docs.python.org/3.5/library/index.html) for your implementation.
## 3. Create your function
It is usually confusing users with how to create their first function project. Therefore we provide a built-in utility `tpfunc` which can help you start with a template `index.py` and `pacakge.json`.
```bash
root@Moxa:/home/moxa# tpfunc init demo
```
```bash
./demo
 +- index.py      # main source file for your function code
 |
 +- package.json  # describes properties for your function
```
- **package.json**
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

> `@name`: function name (should be unique)\
> `@enabled`: start/stop function\
> `@trigger-driven`: the timing starting your function by **dataDriven** or **timeDriven**\
> `@dataDriven`: function starts with **selected tags** **and events**\
> `@timeDriven`: function starts with **boot time** / **interval delay time** / **cron job datetime**\
> `@expose-tags`: the **virtual tags** are about to expose\
> `@params`: **pre-defined parameters** that can be read in your function code

> The value of "trigger/timeDriven/cronJob"(string) follows the standard cron schedule expressions, please refer to https://crontab.guru/


To facility developers, the `init` command comes with three options, `--trigger-time`, `--trigger-data`, `--trigger-http`. `--trigger-time` is used by default in ThingsPro Edge Function.

```
Usage:
  tpfunc init [flags]

Flags:
  -h, --help           help for init
      --trigger-time   init a time trigger template
      --trigger-data   init a data trigger template
      --trigger-http   init a http trigger template
```

- **index.py**
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
## 4. Deploy your function
Now your first function has been created, then we can move on to how to deploy it. According to `tpfunc` usages. There are several related commands for deployment operation. 
```bash
Usage:
  tpfunc [command]
Available Commands:
  add         tpfunc add
  del         tpfunc del
  ls          tpfunc ls
```
### Add function:
A patch command to update your function code. 
```bash
root@Moxa:/home/moxa# ls demo
index.py  package.json
root@Moxa:/home/moxa# tpfunc add demo
```
> If it's the first time to deploy the function, `tpfunc` will auto-create it. If not, the function will be updated by the different parts.\
However, unless the files under your function directory are missing or the format is incorrect, adding function is always successful.\
The next command will show you how to check your function is deployed and running properly.
### List function:
A listing command to get all current functions status.
```bash
root@Moxa:/home/moxa# tpfunc ls
+------------+--------+------+---------------------------+----------+-------------------------+
|    NAME    | ENABLE | MODE |        LASTUPTIME         |  STATE   |          ERROR          |
+------------+--------+------+---------------------------+----------+-------------------------+
| dummy      | false  |      | 2020-11-09T21:59:33+08:00 | inactive | {"message": "inactive"} |
| demo       | true   |      | 2020-11-09T04:33:43+08:00 | running  |                         |
+------------+--------+------+---------------------------+----------+-------------------------+
```

```bash
Usage:
  tpfunc ls [flags]

Flags:
  -a, --all           show all configuration
      --data-driven   show detials of data driven functions
      --time-driven   show details of time driven functions
      --http-proxy    show http proxy configuration
```
### Delete function:
A delete command to remove the target function.
```bash
root@Moxa:/home/moxa# tpfunc del demo
root@Moxa:/home/moxa# tpfunc ls
+------------+--------+------+---------------------------+----------+-------------------------+
|    NAME    | ENABLE | MODE |        LASTUPTIME         |  STATE   |          ERROR          |
+------------+--------+------+---------------------------+----------+-------------------------+
| dummy      | false  |      | 2020-11-09T21:59:33+08:00 | inactive | {"message": "inactive"} |
+------------+--------+------+---------------------------+----------+-------------------------+
```

### Start/Stop function:
start/stop command to make function lifecycle control become easier
```bash
Usage:
  tpfunc start [function_name]
  tpfunc stop [function_name]
```

## 5. Debug functions
During the development and deployment, there always needs a way to the debug.
In ThingsPro Edge Function, a real-time logging channel setup by default when each funciton starts.
As long as user hit the log command `tpfunc log {function_name}`,
the streaming `stdout` and `stderr` will be printed on screen by time sequence.
```bash
root@Moxa:/home/moxa# tpfunc log demo
[2020-11-25T21:28:20+08:00] {'version': '1.0'}
```

## 6. Types of function
### Type 1. Detect events/tags and respond
Once you create the function with `--trigger-data`, you can add those tags and events that you want to detect and respond. This example will listen to a tag `/system/status/cpuUsage` and a event `system/app stop`.

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

# When using the data-driven pattern, the callback function name YOUR_DATA_CALLBACK must match your tpfunc name. Please avoid using names that are against python's rule of function names, such as reserved keywords or operators.
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

ThingsPro Edge supports more than 60+ events, refer to <a href="https://github.com/TPE-TIGER/TPE2-Technical-Document/blob/main/documents/TPE2-EventList.md">the link</a> for detail.

### Type 2. HTTP Server
Some use cases will require accessing the function via an HTTP(s) request. By ThingsPro Edge Function, you can invoke those APIs with an HTTP request using the POST, PUT, GET and DELETE without implement a server, even a ThingsPro application. First, init a function with `tpfunc init http --trigger-http`. Since the API function doesn't have to start repeatly or restart refrequently, `package.json` has been configured as boot mode.

> * Concurrent requests in a RESTful API is not handled.
> * The API authentication is still required, so ensure you have the token before applying the APIs. Besides, a hard prefix `api/v1/tpfunc/` is always ahead of all HTTP function endpoints. `Ex. https://{IP}/api/v1/tpfunc/{PATH}`

This example display a dummy Get method `world/hello` always return `Hello World` message.
- **package.json**
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

- **index.py**
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

### Type 3. PubSub tags

Although we already have provide data trigger callback function, sometimes user prefer handle the function lifecycle on their own. To get the tag without data callback, PubSub pattern is also available in ThingsPro Edge function. In this example, we are going to subscribe a few of tags and scaling the value, then publish them to become a new virtual tag.

First, we define this function is triggered by boot time. Meanwhile, it is also the provider of the virtual tag `modbus_tcp_master/device/di0_scale` that defined in `expose` section.
- **package.json**
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
- **index.py**
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

def callback(_type, data={}):
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
If you already had cloud connectivity in ThingsPro Edge, such as **Sparkplug**, **Azure IoT Edge/Device**, even **generic MQTT**.Now you can open the tag select page, the virtual tag should be listed under the provider name you defined in package.json.

### Type 4: Direct access tag

Although we already have subscribed tag, sometimes user prefer on-demand access read or write tag directly. To get the tag without subcription routine, Access pattern is also available in ThingsPro Edge function. In this example, we are going to directly read and write tag.

Note: Direct access doesn't support system tag.

First, we define this function is triggered by boot time.
- **package.json**
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
Then, we look into `index.py`. Accesser Read Tag API need provider name, source name, and tag name parameters, then get result from  `dataValue` and `dataType` fields of responsed json data. Similarly, Accesser Write Tag API need extra `dataValue` and `dataType` fields. Please be noticed that dataType is enum type of thingspro.edge.tag_v1 library.

- **index.py**
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


### Type 5: Create your own virtual tags


User can self-defined virtual tags in function rule program, and these tags will be auto-generated into Thingspro Edge Tag Service. Thus, we're able to operate these virtual tags by `Taghub` api. e.g. `tags/list`.
Additionally, function progrom SDK also provide simple way let programer to register direct access method of the defined virtual tags. Follow below steps, user can use `tags/access/${ProviderName}/${SourceName}/${TagName}`
to access registered callback function to do read or write operation.

First, we define this function is triggered by boot time.
- **package.json**
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

- **index.py**
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
