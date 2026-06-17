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

# Assign the output of the get_facts()to the variable device_facts
device_facts = device.get_facts()


# Printing each interface separately
print("interface_list:")
for interface in device_facts['interface_list']:
    print(" - ", interface)    # Alternative f-string:  print(f" - {interface}")

device.close()
