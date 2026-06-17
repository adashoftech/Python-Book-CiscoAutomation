# 1. Import the required modules
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli

# 2. Define the task
def run_cli_commands(task):

    commands_to_run = [
        "show version",
        "show ip interface brief"
    ]

# 3. Execute the list of CLI commands on the device using napalm_cli.
    result = task.run(task=napalm_cli, commands=commands_to_run)

# 4. Return the result of napalm_cli which is a dictionary where keys are commands and # values are their outputs.

    return result[0].result # Access the actual dictionary of command outputs

if __name__ == "__main__":

# 5. Initialize Nornir
    nr = InitNornir(config_file="config.yaml")

    print("\n--- Running CLI Commands on Devices ---")
    results = nr.run(task=run_cli_commands)

# 6. Iterate through the results for each host
    for host_name, multi_result in results.items():
        print(f"\n==================================================")
        print(f"Processing results for: {host_name}")
        print(f"==================================================")

        if multi_result.failed:
            print(f"Task failed for {host_name}. Error: {multi_result[0].exception}")
        else:
            command_outputs = multi_result[0].result

            for command, output in command_outputs.items():
                print(f"\n--- Output for command: '{command}' ---")
                print(output)
