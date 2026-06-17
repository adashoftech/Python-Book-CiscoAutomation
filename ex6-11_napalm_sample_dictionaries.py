# 1. Import required library and module
import napalm
from pprint import pprint

# 2. Select network driver
driver = napalm.get_network_driver('ios')

# 3. Create a device object
device = driver( hostname='192.168.1.1',
                 username='admin',
                 password='cisco',
                 optional_args={'secret':'spot'} )

# 4. Establish a connection
device.open()

# 5. Implement NAPALM methods

# Single dictionary:
print('\nSingle dictionary:')

print('\nget_facts()')
print('-' * 11)
pprint(device.get_facts())

pause = input('\nNext get_environment()')

print('\nget_environment()')
print('-' * 17)
pprint(device.get_environment())

pause = input('\nNext get_interfaces()')

# Dictionary of dictionaries:
print('\nDictionary of dictionaries:')

print('\nget_interfaces()')
print('-' * 16)
pprint(device.get_interfaces())

pause = input('\nNext get_interfaces_ip()')

print('\nget_interfaces_ip()')
print('-' * 19)
pprint(device.get_interfaces_ip())

# List of dictionaries:
print('\nList of dictionaries:')

pause = input('\nNext get_arp_table()')

print('\nget_arp_table()')
print('-' * 15)
pprint(device.get_arp_table())

# 6. Close the connection
device.close()
