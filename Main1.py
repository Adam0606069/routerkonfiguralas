from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException

def get_running_config(device_dict, filename):
    try:
        net_connect = ConnectHandler(**device_dict)
        net_connect.enable()
       
        output = net_connect.send_command("show running-config")

        with open(filename, 'w') as f:
            f.write(output)

        print(f"A konfiguráció sikeresen mentve lett: {filename}")
    except NetmikoAuthenticationException as e:
        print(f"Hiba a hitelesítés során: {e}")
    except NetmikoTimeoutException as e:
        print(f"A kapcsolat időtúllépés miatt megszakadt: {e}")
    except (IOError, OSError) as e:
        print(f"Hiba a fájlba írás során: {e}")
    finally:
        # A kapcsolat bontása, még ha hiba történt is
        net_connect.disconnect()



# Több eszköz adatai egy listában
devices=[
    {"host": "192.168.1.1", "username": "admin", "password": "admin", "secret": "cisco", "device_type": "cisco_ios"},
    {"host": "192.168.2.2", "username": "admin", "password": "admin", "secret": "cisco", "device_type": "cisco_ios"}
]

#csatlakozás minden eszközhöz
for device in devices:
    filename="running_config_"+device["host"]+".txt"
    get_running_config(device, filename)