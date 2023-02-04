# Simple TCP socket client

![License](https://img.shields.io/badge/License-BSD%203--Clause-green)
[![Downloads](https://img.shields.io/pypi/dm/simple-socket-client.svg?color=orange)](https://pypi.python.org/pypi/simple-socket-client)
[![Latest Version](https://img.shields.io/pypi/v/simple-socket-client.svg)](https://pypi.python.org/pypi/simple-socket-client)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/simple-socket-client.svg)](https://pypi.python.org/pypi/simple-socket-client)

## Installation

Install it with pip:

```shell
$ pip install simple-socket-client
```

Or you can add it as dependency in requirements.txt file of your python application:

```
simple-socket-client~=1.2
```

## Usage

```python
from simple_socket_client import SimpleSocketClient

client = SimpleSocketClient('192.168.0.2', 6666)
client.connect()

client.send('Test'.encode()) # if you don't need an answer
answer = client.ask('Hi!'.encode())
print(answer.decode())

client.disconnect()
```
