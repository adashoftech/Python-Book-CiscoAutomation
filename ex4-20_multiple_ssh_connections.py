# Import the Netmiko Library
import netmiko

# Assign IP addresses of the devices
device_list = ['192.168.1.1', '192.168.2.2', '192.168.3.2']

# Dictionary to store active connections
connections = {}

# Establish SSH connections to all devices simultaneously
for device in device_list:
    connections[device] = netmiko.ConnectHandler(
        ip=device,
        device_type='cisco_ios',
        username='admin',
        password='cisco',
        secret='spot'  # Enable password if required
    )
    print(f"\nConnected to {device}")

# Execute a command on all devices while all connections remain open
for device, connection in connections.items():
    print(f"\nIPv4 routing table for router with IP address {device}:\n")
    print(connection.send_command('show ip route'))

# Close all SSH connections
for device, connection in connections.items():
    connection.disconnect()
    print(f"\nDisconnected from {device}")

print("\nAll devices processed.")
