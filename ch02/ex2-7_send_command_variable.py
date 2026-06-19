import netmiko

connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Example of directly printing the output of the send_command() method
print('\nDirectly from the print function:')
print(connection.send_command('show ip interface brief'))

# Example of storing the output of the send_command() method in a variable
# The variable cmd_output stores the command result, which is then printed
print('\nPrinting from contents from the variable:')
cmd_output = connection.send_command('show ip interface brief')
print(cmd_output)

connection.disconnect()

