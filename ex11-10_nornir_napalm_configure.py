# 1. Import required modules
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure

# 2. Define the Nornir task function
def configure_interface(task):
    print(f"*** Running configure_interface on {task.host.name} ***")

# 3. Define the configuration snippet to be applied
    config_snippet = """
interface Loopback100
 description Configured by Nornir + NAPALM
"""

# 4. Execute the napalm_configure task
    result = task.run(
        task=napalm_configure,
        configuration=config_snippet,
        replace=False,
        dry_run=False
    )

# 5. Extract the result for the napalm_configure task
    cfg_result = result[0]

# 6. Check for configuration application failure
    if cfg_result.failed:
        print(f"!!! Configuration FAILED on {task.host.name}: {cfg_result.exception} !!!")
        return # Exit the task for this host if it failed

# 7. Report success
    print(f"Configuration applied successfully on {task.host.name}.")


if __name__ == "__main__":
# 8. Initialize Nornir
    nr = InitNornir(config_file="config.yaml")

# 9. Run the 'configure_interface' task across all hosts
    results = nr.run(task=configure_interface)

# 10. Print overall failure status
    print("Any failures overall?:", results.failed)
    print("--- Script finished ---")
