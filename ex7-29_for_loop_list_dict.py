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

device_arp = device.get_arp_table()

print('\nOutput: pprint(device_arp)')
pprint(device_arp)

### **Manually Traversing list of dictionaries**
print('\nEntries in the ARP table:')

# For loop - each item in the list
for entry in device_arp:
    print('\nNew ARP Entry:')

    # Each entry is a dictionary
    for key, value in entry.items():
        print(f'  {key}: {value}')

device.close()
