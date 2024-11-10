import os
import subprocess
from time import sleep
import requests

def checkConn(url: str) -> bool:
    try:
        resp = requests.get(url, timeout=5)
        return resp.status_code == 200
    except:
        return False

# 等待网络
for _ in range(5):
    if checkConn('https://github.com'):break
    sleep(1)

result = subprocess.run(['sudo', 'pacman', '-Sy'],stdout=subprocess.PIPE)
if result.returncode != 0:
    print("<span color=\'red\'>  </span>")
    print('检查更新失败,请检查网络')
    exit()

with os.popen('paru -Qu | wc -l') as c:
    result = c.read().strip()

if result == '0':
    print("<span color=\'green\'>  </span>")
    print("所有软件包均为最新版本")
else:
    print(result)
    print(f'有{result}个软件包需要更新')
