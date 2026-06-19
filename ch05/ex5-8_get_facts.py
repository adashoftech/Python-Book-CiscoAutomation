# 1. Import required library and module
import napalm
from pprint import pprint

# 2. Select network driver
driver = napalm.get_network_driver('ios')

# 3. Create a device object
device = driver(
                hostname='192.168.1.1',
                username='admin',
                password='cisco',
                optional_args={'secret':'spot'}
            )

# 4. Establish a connection
device.open()

# 5. Implement NAPALM methods

print("\nPrint results from get_facts() using pprint(device.get_facts():")
print("-" * 63)
pprint(device.get_facts())

# Assign the output of the get_facts()to the variable device_facts
device_facts = device.get_facts()

print("\nPrint key-value pairs individually using device_facts['key']:")
print("-" * 61)
print("fqdn:", device_facts['fqdn'])
print("hostname:", device_facts['hostname'])
print("interface_list:", device_facts['interface_list'])
print("model:", device_facts['model'])
print("os_version:", device_facts['os_version'])
print("serial_number:", device_facts['serial_number'])
print("uptime:", device_facts['uptime'])
print("vendor:", device_facts['vendor'])

# 6. Close the connection
device.close()
