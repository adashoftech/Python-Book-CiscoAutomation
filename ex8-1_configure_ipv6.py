import napalm
from pprint import pprint

# Load Cisco IOS driver
driver = napalm.get_network_driver('ios')

# Define device
device = driver(
    hostname='192.168.1.1',
    username='admin',
    password='cisco',
    optional_args={'secret': 'spot'}
)

# Open connection to device
device.open()

# View interface configuration before changes
print('\nBefore changes:')
pprint(device.get_interfaces_ip())

# Define IPv6 config as list of IOS CLI commands
ipv6_config = '''

ipv6 unicast-routing

interface GigabitEthernet0/0/0
ipv6 address 2001:db8:c0de:1::1/64
ipv6 address fe80::1 link-local
exit

interface GigabitEthernet0/0/1
ipv6 address 2001:db8:c0de:2::1/64
ipv6 address fe80::1 link-local
exit
'''

# Load configuration into candidate
device.load_merge_candidate(config=ipv6_config)

# Show the differences between running config and candidate config
print('\nStaged changes:')
print(device.compare_config())

# Ask user if they want to commit the changes
user_input = input("\nDo you want to commit these changes? (yes/no): ")

if user_input.lower() == 'yes':
    device.commit_config()
    print('\nChanges committed.')
else:
    device.discard_config()
    print('\nChanges discarded.')

# Verify interface configuration after changes
print('\nAfter changes:')
pprint(device.get_interfaces_ip())

# Close connection
device.close()
