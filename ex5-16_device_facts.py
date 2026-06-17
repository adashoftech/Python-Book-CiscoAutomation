from pprint import pprint

device_facts = {
                'fqdn': 'Router-R1.SSH-KEY.com',
                'hostname': 'Router-R1',
                'interface_list': [ 'GigabitEthernet0/0/0',
                                    'GigabitEthernet0/0/1',
                                    'GigabitEthernet0/0/2',
                                    'GigabitEthernet0'],
                'model': 'ISR4331/K9',
                'os_version': 'ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M),'
                              'Version 16.6.3, RELEASE SOFTWARE (fc8)',
                'serial_number': 'FLM2229W1R6',
                'uptime': 2820.0,
                'vendor': 'Cisco'
               }

pprint(device_facts)



