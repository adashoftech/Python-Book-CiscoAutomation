import netmiko

# The secret parameter is included to allow privileged EXEC mode access
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Save the running configuration to startup configuration
# The save_config() method saves the running configuration without
# requiring user intervention.
# Unlike send_command_expect(), it does not need an expect_string
# since it handles the entire process internally.
print('\nCopy running-config to startup-config, please wait...\n')
connection.save_config()

# Store results to variable including the IOS command
cmd_output = connection.send_command('show startup-config',
                                      strip_command=False)

# Print the current prompt and cmd_output which includes the command and output
print(connection.find_prompt(), cmd_output)

connection.disconnect()
