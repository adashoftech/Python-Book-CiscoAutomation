# Import the Netmiko Library
import netmiko
# Import getpass to securely collect passwords
# without displaying them on the screen
from getpass import getpass

# Prompt user for SSH credentials
# Username is displayed in clear text
username_entered = input('Enter SSH username: ')

# Password is hidden when entered
password_entered = getpass('Enter SSH password: ')

# Enable secret password is also hidden
secret_entered = getpass('Enter enable secret password: ')

# List of device IP addresses (assumes all devices share the same credentials)
device_list = ['192.168.1.1', '192.168.2.2', '192.168.3.2']

# Loop through each device in the list and establish an SSH connection)
for device in device_list:

    # Use the collected credentials to connect to the current device
    connection = netmiko.ConnectHandler(
             ip=device,     # Assign the IP address dynamically
             device_type='cisco_ios',
             username=username_entered, # Use the entered username
             password=password_entered, # Use the entered password
             secret=secret_entered  # Use the entered enable password if required
    )

    # Execute and display the output of the 'show ip interface brief' command
    print("\n'show ip interface brief' for:", device, "\n")
    print(connection.send_command('show ip interface brief'))

    # Close the SSH connection for this device
    connection.disconnect()

print("All devices processed.")
