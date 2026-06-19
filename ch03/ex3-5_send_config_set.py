# Import the Netmiko Library
import netmiko

# Establish an SSH connection to the device
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot') # Enable password)

# Define a list of interface configuration commands
interface_description_list = [
    'interface gig 0/0/0',
    'description LAN interface - used Netmiko',
    'exit',

    'interface gig 0/0/1',
    'description Connection to R2 - used Netmiko',
    'exit'
]

# Enter privileged EXEC mode (required for making configuration changes)
connection.enable()

# Apply the list of configuration commands to the device
connection.send_config_set(interface_description_list)

# Display the IOS command before executing it for clarity
print('\nIOS command: '
      'show running-config | begin interface GigabitEthernet0/0/0')

print(connection.send_command(
      'show running-config | begin interface GigabitEthernet0/0/0'))

# Close the SSH connection
connection.disconnect()
