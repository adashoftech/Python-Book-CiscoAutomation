# Import the Netmiko Library
import netmiko

# Establish an SSH connection to the device
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco')

# Using the connection to send an IOS command
print(connection.send_command('show ip interface brief'))

# Close the SSH connection
connection.disconnect()


