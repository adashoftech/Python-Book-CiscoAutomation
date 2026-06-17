# Import the Netmiko Library
import netmiko

# Assign IP address of the device to a variable
device = '192.168.1.1'

# Establish an SSH connection to the device
connection = netmiko.ConnectHandler(
                    ip=device,     # Assign the IP address using the variable
                    device_type='cisco_ios',
                    username='admin',
                    password='cisco',
                    secret='spot'  # Enable password if required
)

# Send a command to the device and print the output
print(connection.send_command('show ip interface brief'))

# Close the SSH connection
connection.disconnect()


