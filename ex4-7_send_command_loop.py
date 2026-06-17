# Import the Netmiko Library
import netmiko

# Assign IP address of the device to a variable
device_list = ['192.168.1.1', '192.168.2.2']

# Loop through IP addresses
# Assign device to each item in the list of devices (device_list)
for device in device_list:

    # Establish an SSH connection to the device
    connection = netmiko.ConnectHandler(
                    ip=device,     # Assign the IP address using the variable
                    device_type='cisco_ios',
                    username='admin',
                    password='cisco',
                    secret='spot'  # Enable password if required
    )

    # Display the IPv4 routing table
    # send a command to the device and print the output
    print("\nIPv4 routing table for router with the IP address:", device, "\n")
    print(connection.send_command('show ip route'))

    # Close the SSH connection for this device
    connection.disconnect()

print("All devices processed.")
