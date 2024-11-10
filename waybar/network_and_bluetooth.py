import socket
import requests
import psutil
from os import popen
from json import dumps

NET = ' '
WIFI = ' '
NO_VPN = '<span color="orange"> </span>'
CANNOT_USE = '<span color="red"> </span>'
NOIP = '<span color="red"> </span>'

BLUETOOTH = ' '
NO_BLUETOOTH = '<span color="#747474">󰂲 </span>'
BLUETOOTH_CON = '󰂱 '

netText = ''
netTooltip = ''
bluetoothText = ''
bluetoothTooltip = ''

def getIp() -> str|None:
    try:
        # 获取主机名
        hostname = socket.gethostname()
        # 获取IP地址
        ip_address = socket.gethostbyname(hostname)
        if ip_address == '127.0.0.1':return None
        return ip_address
    except socket.error:
        return None

def checkConn(url: str) -> bool:
    try:
        resp = requests.get(url, timeout=5)
        return resp.status_code == 200
    except:
        return False

def useWifi() -> bool:
    net_if_addrs = psutil.net_if_addrs()
    for interface, _ in net_if_addrs.items():
        if interface.startswith('Wi-Fi') or interface.startswith('wlan'):
            return True
    return False


def getNetInfo():
    global netText, netTooltip
    ip = getIp()
    if ip == None:
        netText = NOIP
        netTooltip = '没有找到IP'
        return
    netTooltip = f'ip:{ip}'
    if not checkConn('https://www.baidu.com/'):
        netText = CANNOT_USE
        netTooltip += '\n无法访问网站'
    if not checkConn('https://www.google.com/'):
        netText = NO_VPN
        netTooltip += '\n部分网站访问受限'
    if useWifi():
        netText = WIFI
    else:
        netText = NET

def checkBlue() -> bool:
    with popen('bluetoothctl show')as c:
        result = c.read()
    if 'Powered: yes' in result:
        return True
    else:
        return False

def getBlueDevices() -> list[str]:
    devices = []
    with popen('bluetoothctl devices Connected')as c:
        result = c.read()
    for i in result.split('\n'):
        if not i.startswith('Device'): continue
        _, mac, device = i.split(' ',2)
        devices.append(device)
    return devices

def getBluetoothInfo():
    global bluetoothText, bluetoothTooltip
    if not checkBlue():
        bluetoothText = NO_BLUETOOTH
        bluetoothTooltip = '未开启蓝牙'
        return
    devices = getBlueDevices()
    if len(devices) == 0:
        bluetoothText = BLUETOOTH
        bluetoothTooltip = '蓝牙未连接'
        return
    bluetoothText = BLUETOOTH_CON
    bluetoothTooltip = '\n'.join(['连接的蓝牙设备:',*devices])

getNetInfo()
getBluetoothInfo()
text = netText + '|' + bluetoothText
tooltip = netTooltip + '\n\n' + bluetoothTooltip
# print(text)
# print(tooltip)
print(dumps({'text':text,'tooltip':tooltip}))
