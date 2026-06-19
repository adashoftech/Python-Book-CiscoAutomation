# 1. Import required modules
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config

# 2. Initialize Nornir with the configuration file
nr = InitNornir(config_file='config.yaml')

# 3. Define the configuration commands
commands_list = [
    'ipv6 unicast-routing',
    'ipv6 cef'
]

# 4. Run the task across all hosts
result = nr.run(task=netmiko_send_config, config_commands=commands_list)

# 5. Extract the output of the configuration command for each device
for host, multi_result in result.items():
    print(f'\n\n------{host}------')
    print(multi_result[0].result)


