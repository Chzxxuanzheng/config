from psutil import virtual_memory
from os import popen
def cpu_percent():
    with popen('cat /proc/loadavg')as c:
        return c.read().split(' ')[0]
cpu = cpu_percent()
memory = virtual_memory()[2]
print(f' {cpu}%| {memory}%')
