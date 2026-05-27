from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco"
}

connection = ConnectHandler(**device)

connection.enable()

commands = [
    "hostname BRANCH-R1",
    "interface GigabitEthernet0/0",
    "ip address 10.10.10.1 255.255.255.0",
    "no shutdown",
    "exit"
]

output = connection.send_config_set(commands)

print(output)

save = connection.save_config()
print(save)

connection.disconnect()
