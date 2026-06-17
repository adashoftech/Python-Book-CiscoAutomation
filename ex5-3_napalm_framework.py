# 1. Import required library and module
import napalm
from pprint import pprint

# 2. Select network driver
driver = napalm.get_network_driver('ios')

# 3. Create a device object
device = driver( hostname= '192.168.1.1',
                 username= 'admin',
                 password= 'cisco',
                 optional_args= {'secret':'spot'}
               )

# 4. Establish a connection
device.open()

# 5. Implement NAPALM methods
pprint(device.get_facts())

# 6. Close the connection
device.close()
