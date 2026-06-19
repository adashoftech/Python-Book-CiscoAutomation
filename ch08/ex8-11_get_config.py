import napalm

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

configs = device.get_config()

# Display running-config
print("\nRunning Config:")
print(configs["running"])

# Display startup-config (if available)
if "startup" in configs:
    print("\nStartup Config:")
    print(configs["startup"])
else:
    print("\nStartup config not available on this platform.")


# Close connection
device.close()
