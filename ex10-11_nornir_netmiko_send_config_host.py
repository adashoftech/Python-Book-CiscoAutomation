# 1. Import required modules
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config

# 2. Initialize Nornir with the configuration file
nr = InitNornir(config_file='config.yaml')

# 3. Define the task
def send_config(task_object):
    # Get device-specific config from host data
    config = task_object.host['config_lines']
    task_object.run(task=netmiko_send_config, config_commands=config)

# 4. Run the task across all hosts
result = nr.run(task=send_config)

# 5. Display the configuration results for each device
for host, multi_result in result.items():
    print(f'\n\n------{host}------')
    print(multi_result[1].result)
