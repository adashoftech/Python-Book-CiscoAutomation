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

### **Manually Traversing get_facts() Dictionary**
print('\nKey-Value pairs in the get_facts() dictionary:')

for key, value in device_facts.items():

    # Check if value is a list (e.g., interface_list)
    if isinstance(value, list):
        print(f'{key}:')
        for item in value:
            print(f'   - {item}')
    else:
        # Just print value if string, integer, float, or Boolean
        print(f'{key}: {value}')

device.close()
