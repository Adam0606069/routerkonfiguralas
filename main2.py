#Írj egy programot, ami bejárja a 3 switch-et és mind a háromra beállítja ugyan azt a VTP domain nevet és VTP password-öt.

from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException


devices=[
    {"host": "192.168.1.121", "username": "admin", "password": "admin", "secret": "cisco", "device_type": "cisco_ios"},
    {"host": "192.168.1.122", "username": "admin", "password": "admin", "secret": "cisco", "device_type": "cisco_ios"},
    {"host": "192.168.1.123", "username": "admin", "password": "admin", "secret": "cisco", "device_type": "cisco_ios"}
]




for device in devices:
    net_connect=ConnectHandler(**device)
    net_connect.enable()
    net_connect.send_config_set(["vtp password cisco", "vtp domain moricz.hu"])
    net_connect.disconnect()
