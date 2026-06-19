# Import the Netmiko Library
import netmiko
import os

# Get the current directory path to ensure the program
# can locate the configuration file
my_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the configuration file
config_file = os.path.join(my_directory, 'r1_ipv6_update.txt')

# Establish an SSH connection to the device
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot') # Enable password

# Enter privileged EXEC mode (required for making configuration changes)
connection.enable()

# Display the current interface configuration before applying updates
print('\nIOS command: '
      'show running-config | begin interface GigabitEthernet0/0/0')
print(connection.send_command(
      'show running-config | begin interface GigabitEthernet0/0/0'))

# Apply the configuration commands from the file to the device
# Store the output (including prompts and commands) in cli_output
cli_output = connection.send_config_from_file(config_file)

# Display the full command execution output, including prompts
print(cli_output)

# Display the updated interface configuration after applying the file
print('\nIOS command: '
      'show running-config | begin interface GigabitEthernet0/0/0')
print(connection.send_command(
      'show running-config | begin interface GigabitEthernet0/0/0'))

# Close the SSH connection
connection.disconnect()
