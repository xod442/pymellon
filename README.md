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
m = Management('10.132.0.76','admin','admin')

info = m.get_running_config()

info = json.loads(info)

lines = info['data']['Lines']
for line in lines:
    print(line)

```

## Documentation
[Documentation for Mellanox can be found here](https://support.hpe.com/hpesc/public/docDisplay?docId=a00055729en_us&docLocale=en_US)

## Functions

* `command.py` - Send commands to the switch
* `management.py` - Work with configuration files
* `monitoring.py` - Alerts, incidents, contacts, checks
* `ports.py` - Work with ports
