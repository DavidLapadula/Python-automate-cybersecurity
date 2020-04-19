import random, os, subprocess


def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    mac = ""
    for i in range(0,6):
        rand = f"{get_rand()}{get_rand()}"
        if not i == 5:
            mac += f"{rand}:"
        else:
            mac += f"{rand}"
    return mac

# Find MAC on linux machines
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

subprocess.call(["sudo", "ifconfig", "eth0", "down"])

new_address = new_mac()
subprocess.call(["sudo", "ifconfig", "eth0", "hw", "ether", "%s"%new_address])

subprocess.call(["sudo", "ifconfig", "eth0", "up"])

# New MAC address
print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))
    

