import napalm
from pprint import pprint

# Load Cisco IOS driver
driver = napalm.get_network_driver('ios')

# Define device
device = driver(
    hostname='192.168.1.1',
    username='admin',
    password='cisco',
    optional_args={'secret': 'spot'}
)

# Open connection to device
device.open()

# Define full replacement configuration as a multi-line string
full_replacement_config = '''
version 16.6
service timestamps debug datetime msec
service timestamps log datetime msec
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
!
hostname Router-R1-NEW
!
boot-start-marker
boot-end-marker
!
!
vrf definition Mgmt-intf
 !
 address-family ipv4
 exit-address-family
 !
 address-family ipv6
 exit-address-family
!
enable secret 5 $1$tGx0$PAdygny/8T5W2.xTctqlu0
!
no aaa new-model
!
no ip domain lookup
ip domain name SSH-KEY.com
!
subscriber templating
ipv6 unicast-routing
!
!
multilink bundle-name authenticated
!
license udi pid ISR4331/K9 sn FDO22512ULU
file prompt quiet
diagnostic bootup level minimal
spanning-tree extend system-id
archive
 path flash:backup-config
!
username admin privilege 15 password 0 cisco
!
redundancy
 mode none
!
interface GigabitEthernet0/0/0
 description Updated LAN interface using Netmiko
 ip address 192.168.1.1 255.255.255.0
 negotiation auto
 ipv6 address FE80::1 link-local
 ipv6 address 2001:DB8:C0DE:1::1/64
!
interface GigabitEthernet0/0/1
 description Updated interface to R2 using Netmiko
 ip address 192.168.2.1 255.255.255.0
 negotiation auto
 ipv6 address FE80::1 link-local
 ipv6 address 2001:DB8:C0DE:2::1/64
!
interface GigabitEthernet0/0/2
 no ip address
 shutdown
 negotiation auto
!
interface GigabitEthernet0
 vrf forwarding Mgmt-intf
 no ip address
 shutdown
 negotiation auto
!
ip forward-protocol nd
ip http server
ip http authentication local
ip http secure-server
ip tftp source-interface GigabitEthernet0
ip route 0.0.0.0 0.0.0.0 192.168.2.2
!
ip scp server enable
!
control-plane
!
line con 0
 exec-timeout 0 0
 logging synchronous
 transport input none
 stopbits 1
line aux 0
 stopbits 1
line vty 0 4
 login local
 transport input ssh
line vty 5 15
 login local
 transport input ssh
!
wsma agent exec
!
wsma agent config
!
wsma agent filesys
!
wsma agent notify
!
end
'''

# Stage the replacement configuration
device.load_replace_candidate(config=full_replacement_config)

# Compare the staged configuration to the current running-config
print('\nStaged differences:')
print(device.compare_config())

# Prompt user to commit or discard
user_input = input('\nDo you want to commit this full configuration replacement? (yes/no): ')

if user_input.lower() == 'yes':
    device.commit_config()
    print('\nNew configuration committed.')
else:
    device.discard_config()
    print('\nConfiguration changes discarded.')

# Close connection
device.close()
