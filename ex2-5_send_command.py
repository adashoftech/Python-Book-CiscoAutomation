# Import the Netmiko Library
import netmiko

# Establish an SSH connection to the device
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Using the connection to send IOS commands
print('\nResults from: show ip interface brief')
print(connection.send_command('show ip interface brief'))

print('\nResults from: show version')
print(connection.send_command('show version'))

print('\nResults from: show arp')
print(connection.send_command('show arp'))

# Close the SSH connection
connection.disconnect()


