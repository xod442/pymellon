# pymellon


A python3 API for interacting with the Mellanox RESt client

## Configuration

Simple installation:

```
pip3 install pymellon
```
You can reference the Mellanox API documentation to see examples of what gets
returned when you make a request.

**Note** :you will need to import pymellon into your python script.

```
from pymellon.command import Command

# Create an instance of the command class, pass credentials
cmd = Command(host,username,password)

# Call the API

comm = 'show interfaces'

info = cmd.send_command(comm)

```

## Documentation
[Documentation for Mellanox can be found here](https://support.hpe.com/hpesc/public/docDisplay?docId=a00055729en_us&docLocale=en_US)

## Functions

* `command.py` - Send commands to the switch
* `management.py` - Work with configuration files
* `monitoring.py` - Alerts, incidents, contacts, checks
* `ports.py` - Work with ports
