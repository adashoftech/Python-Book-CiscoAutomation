# 1. Import required modules
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

# 2. Initialize Nornir with the configuration file
nr = InitNornir(config_file='config.yaml')

# 3. Run the task across all hosts
result = nr.run(
   task=netmiko_send_command,
   command_string='show ip interface brief'
)

# 4. Display the output for each device
for host, multi_result in result.items():
   print(f'\n\n------{host}------')
   print(multi_result[0].result)

