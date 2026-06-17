import netmiko
import time  # Add this import to use sleep()


# The secret parameter is provided, but the enable() method
# has been purposely commented out.
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot',
                                    session_log='my_session_log2.txt')

# The enable() method is required to enter privileged EXEC mode ('Router-R1#').
# It has been commented out here to demonstrate the impact of not using it.
# connection.enable()

# Attempt to save the running configuration to startup configuration
# The copy running-config startup-config command requires privileged EXEC
# mode to execute.
# Without successfully entering privileged mode, this command will fail.
print(connection.send_command_expect('copy running-config startup-config',
                                     expect_string='Destination filename'))

print('Success!')

connection.disconnect()
# Optional but recommended to ensure the session log is written before script exits
time.sleep(1)

# Explicitly close the session log file (flushes remaining output)
if connection.session_log_file:
    connection.session_log_file.close()
