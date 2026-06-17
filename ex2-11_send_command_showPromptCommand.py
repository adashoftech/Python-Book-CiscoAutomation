import netmiko

connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Store results to variable including the IOS command 'show ip interface brief'
cmd_output = connection.send_command('show ip interface brief',
                                      strip_command=False)

# Using find_prompt() to display the device's current prompt
# (e.g., "Router-R1>")
# The value of cmd_output is displayed on a separate line
print(connection.find_prompt())
print(cmd_output)
print('\n')

# Using find_prompt() and send_command() together
# This demonstrates how to display the device prompt followed by the
# command output, making the result look more like the native IOS CLI output.
print(connection.find_prompt(), cmd_output)

connection.disconnect()
