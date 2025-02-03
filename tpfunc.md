# Using `tpfunc` Command

## Table of Contents
- [Using `tpfunc` Command](#using-tpfunc-command)
  - [Table of Contents](#table-of-contents)
  - [3. Create your function](#3-create-your-function)
  - [4. Deploy your function](#4-deploy-your-function)
    - [Add function:](#add-function)
    - [List function:](#list-function)
    - [Delete function:](#delete-function)
    - [Start/Stop function:](#startstop-function)
  - [5. Debug functions](#5-debug-functions)

## 3. Create your function
It is usually confusing users with how to create their first function project. Therefore we provide a built-in utility `tpfunc` which can help you start with a template `index.py` and `pacakge.json`.

> Notice: The `tpfunc` requires root access to run. Currently, we do not support running these functions with `sudo`.For example, the following command will not work:
>```bash
>User@moxa:~$ sudo tpfunc ls
>```

You can use `tpfunc init <function-name>` to create your first function. For example:

```bash
root@Moxa:/home/moxa# tpfunc init demo
```
After executing this command, a basic sample with function name "demo" will be created.
```bash
./demo
 +- index.py      # main source file for your function code
 +- package.json  # describes properties for your function
```

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
