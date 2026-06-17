import netmiko

connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot') # Enable password

# send_command() for configuration is similar to CLI
# secret password is required
connection.enable()

# Global config mode
connection.config_mode()

# Global configuration command
connection.send_command('ip route 0.0.0.0 0.0.0.0 192.168.2.2')

# Exit global config mode
connection.exit_config_mode()

# Verify running-config
print('\nIOS command: show running-config | include ip route')
print(connection.send_command('show running-config | include ip route'))

# Verify routing table
print('\nIOS command: show ip route | begin Gateway')
print(connection.send_command('show ip route | begin Gateway'))

connection.disconnect()

