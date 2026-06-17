import napalm
from pprint import pprint

driver = napalm.get_network_driver('ios')

device = driver(
                hostname='192.168.1.1',
                username='admin',
                password='cisco',
                optional_args={'secret':'spot'}
            )

device.open()

device_environment = device.get_environment()

print('\nOutput: pprint(device_environment)')
pprint(device_environment)

### **Manually Traversing dictionary with nested dictionaries and lists**
print('\nKey-Value pairs with nested dictionaries and lists:')

# For loop - first level key and first level value pairs
for first_level_key, first_level_value in device_environment.items():
    # Print first-level key
    print('\nFirst-level key:')
    print(f'{first_level_key}:')

    # Check if value is a list (e.g., interface_list)
    if isinstance(first_level_value, list):
        for item in first_level_value:
            print(f'   - {item}')

    # Nested 2 levels (one for loop for each level)
    # If value is another dictionary, go deeper
    elif isinstance(first_level_value, dict):

        # For loop - second level key and second level value pairs
        for second_level_key, second_level_value in first_level_value.items():
            # Print second-level key
            print('\n    Second-level key:')
            print(f'    {second_level_key}:')

            # If this is also a dictionary, go one more level
            if isinstance(second_level_value, dict):
      
                # For loop - third level key and third level value pairs
                for third_level_key, third_level_value in \
                    second_level_value.items():
                    # Print third-level key and third-level value
                    print('\n        Third-level key and value:')
                    print(f'        {third_level_key}: {third_level_value}')
            else:
                # Second level Value is not a list or dictionary
                print('\n        Second-level Value:')
                print(f'        {second_level_value}')
    else:

        # Print single value (assuming not a list or dictionary)
        # If first-level value is not a list or dictionary, print it directly
        print(f'    {first_level_value}')

device.close()
