from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.3",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

connection = ConnectHandler(**device)

connection.enable()

bgp_commands = [
    "router bgp 65001",
    "neighbor 192.168.100.2 remote-as 65002",
    "neighbor 192.168.100.2 description ISP-UPLINK",
    "network 10.10.10.0 mask 255.255.255.0",
    "exit"
]

output = connection.send_config_set(bgp_commands)

print(output)

save = connection.save_config()
print(save)

connection.disconnect()
