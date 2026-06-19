# Import the Netmiko Library
import netmiko

# List of device IP addresses
device_list = ['192.168.1.1', '192.168.20.1', '192.168.3.2']

# Loop through each device in the list and attempt an SSH connection
for device in device_list:
    try:
        # Attempt to establish an SSH connection to the device
        connection = netmiko.ConnectHandler(
                    ip=device,        # Assign IP address
                    device_type='cisco_ios', # Specify the device type
                    username='admin', # SSH username
                    password='cisco', # SSH password
                    secret='spot'     # Enable password if required
        )

        # Send the 'show ip interface brief' command and
        # display the output
        print("\nInterface information for:", device, "\n")
        print(connection.send_command('show ip interface brief'))

        # Close the SSH connection for this device
        connection.disconnect()

    # Handle connection timeout errors (e.g., unreachable device,
    # firewall blocking access)
    except netmiko.exceptions.NetmikoTimeoutException:
        print('\nTimeout occurred to', device)
        print('''Common causes of this problem are:
        1. Incorrect hostname or IP address.
        2. Wrong TCP port.
        3. Intermediate firewall blocking access.''')
        print('\n')

    # Handle authentication errors (e.g., wrong username/password)
    except netmiko.exceptions.NetMikoAuthenticationException:
        print('\nAuthentication error', device)
        print('''Common causes of this problem are:
        1. Invalid username and password
        2. Incorrect SSH-key file
        3. Connecting to the wrong device''')
        print('\n')

    # Handle read timeout errors (e.g., device prompt not detected)
    except netmiko.exceptions.ReadTimeout:
        print('\nRead timeout. pattern not detected', device)
        print('''Common causes of this problem are:
        1. Missing or incorrect secret password in ConnectHandler()
        2. Adjust the regex pattern to better identify the terminating
           string. Note, in many situations the pattern is
           automatically based on the network device's prompt.
        3. Increase the read_timeout to a larger value.''')
        print('\n')

    # Catch-all exception handler for any other unexpected errors
    except Exception as e:
        print("An error occurred:", str(e))
