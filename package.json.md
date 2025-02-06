# `package.json` Specification

## Table of Contents
- [`package.json` Specification](#packagejson-specification)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Configuration Structure](#configuration-structure)
  - [Parameter Descriptions](#parameter-descriptions)
    - [General Settings](#general-settings)
    - [Trigger Configuration](#trigger-configuration)
    - [Expose Tags](#expose-tags)
    - [Parameters](#parameters)

## Overview
This configuration file defines the settings for a function, including its name, trigger mechanism, exposed tags, and parameters.

## Configuration Structure
```json
{
  "name": "<string>",
  "enabled": <boolean>,
  "trigger": {
    "driven": "<string>",          // ["dataDriven", "timeDriven"]
    "dataDriven": {
      "tags": { "<provider>": { "<source>": [ "<tag-name>", ... ] } },
      "events": { "<category>": [ "<event-name>", ... ] }
    },
    "timeDriven": {
      "mode": "<string>",          // ["boot", "interval", "cronJob"]
      "intervalSec": <integer>,
      "cronJob": "<string>"
    }
  },
  "expose": {
    "tags": [
      {
        "prvdName": "<string>",
        "srcName": "<string>",
        "tagName": "<string>",
        "dataType": "<string>",    // ["double", "integer", "string"]
        "access": "<string>"       // ["r", "rw"]
      }
    ]
  },
  "params": {
    "<key>": "<value>"
  }
}
```

## Parameter Descriptions
### General Settings
| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `name` | `string` | A unique function name. |
| `enabled` | `boolean` | Enables (`true`) or disables(`false`) the function. |

### Trigger Configuration
| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `trigger.driven` | `string` | Defines when the function should start. Supported values: `"dataDriven"`, `"timeDriven"`. |
| `trigger.dataDriven.tags` | `object` | Defines data-driven triggers based on monitored tags. |
| `trigger.dataDriven.events` | `object` | Defines data-driven triggers based on events. |
| `trigger.timeDriven.mode` | `string` | Defines the time-based trigger mode. Supported values: `"boot"`, `"interval"`, `"cronJob"`.
| `trigger.timeDriven.intervalSec` | `integer` | Specifies the execution interval (in seconds) when `"interval"` mode is selected. |
| `trigger.timeDriven.cronJob` | `string` | Specifies a cron expression for execution when `"cronJob"` mode is selected. |

#### Format for `dataDriven` Triggers
```json
"dataDriven": {
  "tags": {
    "<provider>": {
      "<source>": [ "<tag-name>", ... ]
    }
  },
  "events": {
    "<category>": [ "<event-name>", ... ]
  }
}
```
* `tags`: Defines the monitored data points that trigger the function when they change.
  * `<provider>`: The provider of the data source (e.g., "system").
  * `<source>`: The data source within the provider (e.g., "status").
  * `[ <tag-name>, ... ]`: A list of tags from the source to monitor for changes (e.g., "cpuUsage").
* `events`: Defines the monitored events that trigger the function.
  * `<category>`: The category of the event (e.g., "system").
  * `[ <event-name>, ... ]`: A list of event names from the category that trigger execution (e.g., "app stop").

#### Example:
```json
"dataDriven": {
  "tags": {
    "system": {
      "status": [
        "cpuUsage"
      ]
    }
  },
  "events": {
    "system": [
      "app stop"
    ]
  }
}
```

### Expose Tags
| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `expose.tags` | `array` | Defines the virtual tags to be exposed during the function lifecycle. |

#### Format for the Object of `tags` Array
```json
{
  "prvdName": "<string>",
  "srcName": "<string>",
  "tagName": "<string>",
  "dataType": "<string>",
  "access": "<string>"
}
```
| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `prvdName` | `string` | Data provider name |
| `srcName` | `string` | Data source identifier |
| `tagName` | `string` | Virtual tag name |
| `dataType` | `string` | Data type (valid values: `uint8`, `uint16`, `uint32`, `uint64`, `int8`, `int16`, `int32`, `int64`, `float`, `double`, `string`, `boolean`, `byte-array`, `raw`) |
| `access` | `string` | Access permission (`"r"` for read-only, `"rw"` for read-write) |

#### Example:
```json
{
  "expose": {
    "tags": [
      {
        "prvdName": "virtual",
        "srcName": "cpu",
        "tagName": "onchange",
        "dataType": "double",
        "access": "rw"
      }
    ]
  }
}
```

### Parameters
| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `params` | `object` | Predefined parameters that can be used within the function code. |

#### Example:
```json
"params": {
  "version": "1.0"
}
```