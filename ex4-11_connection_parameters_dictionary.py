# Import the Netmiko Library
import netmiko

# Define device dictionaries containing ConnectHandler parameters
r1 = {
    'ip': '192.168.1.1',   # IP address of Router 1
    'device_type': 'cisco_ios', # Device type for Netmiko
    'username': 'admin',   # SSH username
    'password': 'cisco',   # SSH password
    'secret': 'spot'       # Enable mode password
}

r2 = {
    'ip': '192.168.2.2',   # IP address of Router 2
    'device_type': 'cisco_ios',
    'username': 'rick',
    'password': 'ucsc',
    'secret': 'cabrillo'
}

r3 = {
    'ip': '192.168.3.2',   # IP address of Router 3
    'device_type': 'cisco_ios',
    'username': 'adrian',
    'password': 'cisco',
    'secret': 'devnet'
}

# List of devices - each dictionary represents a
# router's connection parameters
devices = [r1, r2, r3]

print('\n')

# Iterate over each device in the list
for device in devices:

    # Use dictionary unpacking (**) to pass key-value
    # pairs as keyword arguments to ConnectHandler
    connection = netmiko.ConnectHandler(**device)

    # Print the IP address of the connected device
    print("Device IP address:", device['ip'])
    print('-' * 35)  # Print 35 dashes for readability

    # Send the 'show ip interface brief' command and display the output
    output = connection.send_command('show ip interface brief')
    print(output)

    print('\n')
    connection.disconnect()
