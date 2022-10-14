import json
import requests
import pymellon


from pymellon.command import Command
from pymellon.management import Management
from pymellon.ports import Ports

c = Command('10.132.0.76','admin','admin')

comm = 'vlan 666'
info = c.send_command(comm)
info = json.loads(info)
print(type(info))
print(info)



print("---------------------------------------------------------------")
m = Management('10.132.0.76','admin','admin')

info = m.get_running_config()

info = json.loads(info)
print(type(info))
print(info['data']['Lines'])
lines = info['data']['Lines']
for line in lines:
    print(line)

print("---------------------------------------------------------------")
p = Ports('10.132.0.76','admin','admin')
port = '1/16'
info = p.get_port_info(port)
info = json.loads(info)
print(type(info))
print(info)
