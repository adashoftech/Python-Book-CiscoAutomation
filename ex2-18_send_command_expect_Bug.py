import netmiko

# The secret parameter is intentionally omitted in this example.
# This will cause an issue when attempting to use enable() to
# enter privileged EXEC mode.
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',

                                    session_log='my_session_log.txt')

# Attempt to enter privileged EXEC mode without providing a secret password.
# Since the secret parameter is missing, the enable() method will fail,
# and privileged commands will not work.
connection.enable()

# The IOS command, copy running-config startup-config, requires
# privileged EXEC mode access.
print(connection.send_command_expect('copy running-config startup-config',
                                     expect_string='Destination filename'))

print('Success!')

connection.disconnect()
