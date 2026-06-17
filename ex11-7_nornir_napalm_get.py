# 1. Import required modules
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get

# 2. Define the task
def get_device_facts(task):
    print(f"--- Attempting to get facts for {task.host.name} ---")
    try:
# 3. Use NAPALM to retrieve facts
        result = task.run(task=napalm_get, getters=["facts"])

# 4. Check if the task was successful and returned data
        if result.failed:
            print(f"!!! Task FAILED for {task.host.name}: {result.exception} !!!")
            return

# 5. The result is a MultiResult object, with each sub-result containing the data
        facts = result[0].result['facts']

        print(f"--- Successfully retrieved facts for {task.host.name} ---")
        print(f"  Hostname: {facts.get('hostname', 'N/A')}")
        print(f"  Vendor: {facts.get('vendor', 'N/A')}")
        print(f"  OS Version: {facts.get('os_version', 'N/A')}")
        print(f"  Uptime: {facts.get('uptime', 'N/A')} seconds")
        print("-" * 40)

# 6. Catch any unexpected errors gracefully
    except Exception as e:
        print(f"!!! An unexpected error occurred for {task.host.name}: {e} !!!")

if __name__ == "__main__":
# 7. Initialize Nornir
    nr = InitNornir(config_file="config.yaml")

# 8. Run the task
    results = nr.run(task=get_device_facts)

    print("\n--- Script Finished ---")
