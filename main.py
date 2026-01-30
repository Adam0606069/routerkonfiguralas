from netmiko import ConnectHandler

device={
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
    "secret": "cisco",
    "device_type": "cisco_ios"
}

net_connect=ConnectHandler(**device)
net_connect.enable()

#config parancsok kezdete
net_connect.send_config_set(["hostname R1", "banner motd #Jogosulatlan hozzaferes tilos!#"])
output=net_connect.send_command("show running-config")
print(output)
#config parancsok vége
net_connect.send_config_set(["end"])