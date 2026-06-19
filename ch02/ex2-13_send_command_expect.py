import netmiko

# The secret parameter is required for privileged EXEC mode access.
# It provides the password that will be used with the enable command
# to enter privileged mode.
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Ensure privileged EXEC mode
# The enable() method is necessary to enter privileged EXEC mode ('Router#').
# Commands like 'copy running-config startup-config' require this mode
# to execute successfully.
connection.enable()

# Using send_command_expect() to handle interactive prompts
# The expect_string parameter specifies the prompt Netmiko
# should wait for before proceeding.
print(connection.send_command_expect('copy running-config startup-config',
                                     expect_string='Destination filename'))

print('Success!')

connection.disconnect()
