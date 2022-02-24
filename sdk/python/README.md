# ThingsPro Edge Function SDK

ThingsPro Edge Function SDK provides several APIs to interact with ThingsPro Edge features.

- Tag (v1)
  - PubSub
  - Direct Access
- Http Server (v1)
  - Get
  - Post
  - Put
  - Delete

Besides, SDK written in Python3.5, theoretically compatible with all other modules which you can refer to [Python3.5 official website](https://docs.python.org/3.5/library/index.html).

# Release Note
## 2021-07-26 V1.2.3
### Bug Fix:
- fix: can't receive messages after tag_v1 subscribe callback exception

## 2021-07-23 V1.2.2
### Bug Fix:
- fix: tag_v1 subscribe init always run into exception