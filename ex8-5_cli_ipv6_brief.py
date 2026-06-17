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

# Send the "show ipv6 interface brief" command and pretty-print the full dictionary output
print('\nOutput from: device.cli(["show ipv6 interface brief"])')
pprint(device.cli(['show ipv6 interface brief']))

# Send the same command again and store the dictionary output in a variable
output_v6 = device.cli(['show ipv6 interface brief'])

# Print only the command output text (accessing the value inside the dictionary)
print('\nOutput from: output_v6["show ipv6 interface brief"]')
print(output_v6['show ipv6 interface brief'])
   
# Close connection
device.close()
