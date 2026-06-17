import netmiko

connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Using the send_command() method with strip_command=False
# Setting strip_command=False ensures that the executed command
# ('show ip interface brief') is included in the output,
# making it clear what command generated the results.
print('\nPrinting from contents from the variable (including the command):')
cmd_output = connection.send_command('show ip interface brief',
                                      strip_command=False)
print(cmd_output)

connection.disconnect()

