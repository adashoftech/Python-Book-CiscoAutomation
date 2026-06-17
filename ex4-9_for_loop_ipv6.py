# Import the Netmiko Library
import netmiko


# List of interface configuration commands for each router
r1_ipv6_addressing = [
    'ipv6 unicast-routing',   # Enable IPv6 routing

    # Configure IPv6 addresses on GigabitEthernet0/0/0
    'interface gig 0/0/0',
    'ipv6 address 2001:db8:c0de:1::1/64', # Assign global IPv6 address
    'ipv6 address fe80::1:1 link-local',  # Assign link-local address
    'exit',

    # Configure IPv6 addresses on GigabitEthernet0/0/1
    'interface gig 0/0/1',
    'ipv6 address 2001:db8:c0de:2::1/64', # Assign global IPv6 address
    'ipv6 address fe80::1:2 link-local',  # Assign link-local address
    'exit'
]

r2_ipv6_addressing = [
    'ipv6 unicast-routing',   # Enable IPv6 routing

    # Configure IPv6 addresses on GigabitEthernet0/0/0
    'interface gig 0/0/0',
    'ipv6 address 2001:db8:c0de:3::1/64', # Assign global IPv6 address
    'ipv6 address fe80::2:1 link-local',  # Assign link-local address
    'exit',

    # Configure IPv6 addresses on GigabitEthernet0/0/1
    'interface gig 0/0/1',
    'ipv6 address 2001:db8:c0de:2::2/64', # Assign global IPv6 address
    'ipv6 address fe80::2:2 link-local',  # Assign link-local address
    'exit'
]

r3_ipv6_addressing = [
    'ipv6 unicast-routing',   # Enable IPv6 routing

    # Configure IPv6 addresses on GigabitEthernet0/0/0
    'interface gig 0/0/0',
    'ipv6 address 2001:db8:c0de:4::1/64', # Assign global IPv6 address
    'ipv6 address fe80::3:1 link-local',  # Assign link-local address
    'exit',

    # Configure IPv6 addresses on GigabitEthernet0/0/1
    'interface gig 0/0/1',
    'ipv6 address 2001:db8:c0de:3::2/64', # Assign global IPv6 address
    'ipv6 address fe80::3:2 link-local',  # Assign link-local address
    'exit'
]

# List of router management IP addresses
device_list = ['192.168.1.1', '192.168.2.2', '192.168.3.2']

# Loop through each router in the list and apply the correct configuration
for device in device_list:

    # Establish an SSH connection to the device
    connection = netmiko.ConnectHandler(
                    ip=device,     # Assign the IP address using the variable
                    device_type='cisco_ios',
                    username='admin',
                    password='cisco',
                    secret='spot'  # Enable password if required
    )

    # Enter privileged EXEC mode (required for making configuration changes)
    connection.enable()

    # Apply the appropriate IPv6 configuration commands based on the
    # router's IP address
    if device == '192.168.1.1':
        print("\nConfiguring device:",device)
        connection.send_config_set(r1_ipv6_addressing) # Apply R1 IPv6 config
        print(connection.send_command('show ipv6 interface brief')) # Verify

    elif device == '192.168.2.2':
        print("\nConfiguring device:",device)
        connection.send_config_set(r2_ipv6_addressing) # Apply R2 IPv6 config
        print(connection.send_command('show ipv6 interface brief')) # Verify

    elif device == '192.168.3.2':
        print("\nConfiguring device:",device)
        connection.send_config_set(r3_ipv6_addressing) # Apply R3 IPv6 config
        print(connection.send_command('show ipv6 interface brief')) # Verify

    else:
        print("Mismatch of device address and list")


    # Close the SSH connection for this device
    connection.disconnect()

print("All devices processed.")
