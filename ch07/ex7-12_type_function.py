import napalm
from pprint import pprint

driver = napalm.get_network_driver('ios')

device = driver(
                hostname='192.168.1.1',
                username='admin',
                password='cisco',
                optional_args={'secret':'spot'}
            )

device.open()

device_facts = device.get_facts()

for key, value in device_facts.items():
    print(f'{key} is of type {type(value)}')

device.close()

