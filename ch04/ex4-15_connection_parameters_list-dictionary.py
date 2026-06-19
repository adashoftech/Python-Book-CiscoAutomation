# Import the Netmiko Library
import netmiko

# Define a list of dictionaries, each containing connection
# details for a router
devices = [

{
    'ip': '192.168.1.1',   # IP address of Router 1
    'device_type': 'cisco_ios', # Device type for Netmiko
    'username': 'admin',   # SSH username
    'password': 'cisco',   # SSH password
    'secret': 'spot'       # Enable mode password
},

{
    'ip': '192.168.2.2',   # IP address of Router 2
    'device_type': 'cisco_ios',
    'username': 'rick',
    'password': 'ucsc',
    'secret': 'cabrillo'
},

{
    'ip': '192.168.3.2',   # IP address of Router 3
    'device_type': 'cisco_ios',
    'username': 'adrian',
    'password': 'cisco',
    'secret': 'devnet'
}

]

# Loop through each device in the list and establish an SSH connection
for device in devices:

    # Use dictionary unpacking (**) to pass key-value pairs from the dictionary
    # as keyword arguments to Netmiko's ConnectHandler function
    connection = netmiko.ConnectHandler(**device)

    # Print the IP address of the connected device
    print("Device IP address:", device['ip'])
    print('-' * 35)  # Print 35 dashes for readability

    # Send the 'show ip interface brief' command and display the output
    output = connection.send_command('show ip interface brief')
    print(output)

    print('\n')
    connection.disconnect()
