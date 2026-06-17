# Import the Netmiko Library
import netmiko

# Establish an SSH connection to the device
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot') # Enable password)

# Define a list of IPv6 configuration commands
ipv6_configuration_list = [
    'ipv6 unicast-routing',   # Enable IPv6 routing

    # Configure IPv6 addresses on GigabitEthernet0/0/0
    'interface gig 0/0/0',
    'ipv6 address 2001:db8:cafe:1::1/64', # Assign global IPv6 address
    'ipv6 address fe80::1:1 link-local',  # Assign link-local address
    'exit',

    # Configure IPv6 addresses on GigabitEthernet0/0/1
    'interface gig 0/0/1',
    'ipv6 address 2001:db8:cafe:2::1/64', # Assign global IPv6 address
    'ipv6 address fe80::2:1 link-local',  # Assign link-local address
    'exit'
]

# Enter privileged EXEC mode (required for making configuration changes)
connection.enable()

# Apply the list of configuration commands to the device
# Store the output (including prompts and commands) in cli_output
cli_output = connection.send_config_set(ipv6_configuration_list)

# Display the full command execution output, including prompts
print(cli_output)

# Display the IOS command before executing it for clarity
print('\nIOS command: show ipv6 interface brief')

# Verify IPv6 interface configuration commands
print(connection.send_command('show ipv6 interface brief'))

# Close the SSH connection
connection.disconnect()
