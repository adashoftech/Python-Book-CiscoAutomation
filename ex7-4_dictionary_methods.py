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

# Example of using .keys() method
print('\nKeys in the dictionary:')
print(device_facts.keys())

print('\nKeys in the dictionary using a for loop:')
for key in device_facts.keys():
    print(f'Key: {key}')

# Example of using .values() method
print('\nValues in the dictionary:')
print(device_facts.values())

print('\nValues in the dictionary using a for loop:')
for value in device_facts.values():
    print(f'Value: {value}')

# Example of using .items() method
print('\nKey-Value pairs in the dictionary:')
print(device_facts.items())

print('\nKey-Value pairs in the dictionary using a for loop:')
for key, value in device_facts.items():
    print(f'{key}: {value}')

device.close()
