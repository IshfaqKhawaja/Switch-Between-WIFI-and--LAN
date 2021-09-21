import os
import subprocess
from time import sleep


def connect_to_wifi(name, password, index):
    print("Attempting to connect to network at network {}".format(index))
    cmd = 'nmcli dev wifi connect {} password {}'.format(name, password)
    print(cmd)
    output = os.system(cmd)
    print(output)
    print(index)
    if output == 0:
        print("Connection Started at WIFI {}....".format(index))
        while True:
            try:
                ping = subprocess.check_output(
                    'ping -c 1 google.com', shell=True).decode('utf-8')

                print(ping)
                print("Network connected is {}".format(index))
                sleep(1)
            except subprocess.CalledProcessError as e:
                print("Error "+str(e))
                if index == 0:
                    connect(1)
                else:
                    connect(0)


def connect(index):
    name = wifi_name[index]
    print("Trying to establish new Connection  at {}! ".format(name))
    result = subprocess.check_output(
        'ifconfig | more', shell=True).decode('utf-8')
    wifi1 = result.find(name)
    if wifi1 != -1:
        print(wifi1)
        connect_to_wifi(cred[index][0], cred[index][1], index)
    else:
        if index == 0:
            connect(1)
        else:
            connect(0)


wifi_name = ['wlp2s0', 'wlx00304fa11bec']
# ['NS', 'velocis@jmi']
cred = [['HCL', 'zubair2020'], ['OPPO', '13048100312']] #Enter Wifi and LAN credentials
connect(1)
