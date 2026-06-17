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

if device_facts['interface_list'] is None:
    print('interface_list has no data (None)')
elif isinstance(device_facts['interface_list'], list):
    print('interface_list is a list')
elif isinstance(device_facts['interface_list'], dict):
    print('interface_list is a dictionary')
elif isinstance(device_facts['interface_list'], float):
    print('interface_list is a float')
elif isinstance(device_facts['interface_list'], int):
    print('interface_list is an integer')
elif isinstance(device_facts['interface_list'], bool):
    print('interface_list is a boolean')
elif isinstance(device_facts['interface_list'], str):
    print('interface_list is a string')
else:
    print('Unknown data type')

device.close()
