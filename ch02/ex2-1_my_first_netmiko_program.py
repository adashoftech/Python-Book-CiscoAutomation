# My first Netmiko program
import netmiko
 
connection = netmiko.ConnectHandler(ip='192.168.1.1',
                                    device_type='cisco_ios',
                                    username='admin',
                                    password='cisco',
                                    secret='spot')
 
print(connection.send_command('show ip interface brief'))
 
connection.disconnect()

