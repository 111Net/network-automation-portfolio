from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

connection = ConnectHandler(**device)

connection.enable()

ospf_commands = [
    "router ospf 1",
    "router-id 1.1.1.1",
    "network 10.10.10.0 0.0.0.255 area 0",
    "network 172.16.0.0 0.0.255.255 area 0",
    "exit"
]

output = connection.send_config_set(ospf_commands)

print(output)

save = connection.save_config()
print(save)

connection.disconnect()
