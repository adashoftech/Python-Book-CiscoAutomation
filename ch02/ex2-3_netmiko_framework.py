# Step 1: Import the Netmiko Library
# The Netmiko library provides SSH connectivity to network devices for automation.
import netmiko

# Step 2: Establish an SSH connection to the device
# The ConnectHandler method creates a connection using the provided device parameters.

connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')

# Step 3: Execute an IOS command and display the output
# The send_command() method sends the 'show ip interface brief' command to the device.
print ( connection.send_command ( 'show ip interface brief' ) )

# Step 4: Close the SSH connection
# The disconnect() method gracefully terminates the connection.
connection.disconnect()

