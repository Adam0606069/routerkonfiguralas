from netmiko import ConnectHandler

device={
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
    "secret": "admin",
    "device_type": "cisco_ios"
}

net_connect=ConnectHandler(**device)
net_connect.enable()

#config parancsok kezdete
net_connect.send_config_set(["hostname R13", "banner motd #Jogosulatlan hozzaferes tilos!#"])
output=net_connect.send_command("show running-config")
print(output)

with open("running_config.txt", "w", encoding="utf-8") as f:
	f.write(output)
	
output2=net_connect.send_command("show running-config | section interface")

with open("running_config_interfaces.txt", "w", encoding="utf-8") as f:
	f.write(output2)


#config parancsok vége
net_connect.send_config_set(["end"])