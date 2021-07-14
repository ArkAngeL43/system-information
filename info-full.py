#SYSTEM INFO

import os
import sys 
import tabulate 
import psutil 
import platform 
import time 
import datetime 
from datetime import datetime 

os.system(' clear ')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#sys 
print("="*40,"System Information", "="*40)
uname = platform.uname()
time.sleep(0.1)
print(f"System: {uname.system}")
time.sleep(0.1)
print(f"Node Name: {uname.node}")
time.sleep(0.1)
print(f"Release: {uname.release}")
time.sleep(0.1)
print(f"Version: {uname.version}")
time.sleep(0.1)
print(f"Machine: {uname.machine}")
time.sleep(0.1)
print(f"Processor: {uname.processor}")  
time.sleep(1)
#boot t
time.sleep(0.1)
print("="*40, "Bootup Time", "="*40)
time.sleep(0.1)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
time.sleep(0.1)
print(f"Boot Time is: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
time.sleep(0.1)
print("="*40, "CPU Info", "="*40)
#CPU
time.sleep(0.1)
print("Physical cores:", psutil.cpu_count(logical=False))
time.sleep(0.1)
print("Total Cores:", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
time.sleep(0.1)
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
time.sleep(0.1)
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
time.sleep(0.1)
print(f"CUrrent Frequency: {cpufreq.current:.2f}Mhz")
time.sleep(0.1)
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
time.sleep(0.1)
print(f"Total CPU Usage: {psutil.cpu_percent()}%") 
time.sleep(1.5)
#memory
time.sleep(0.1)
print("="*40, "Memory Information", "="*40)
svmem = psutil.virtual_memory()
time.sleep(0.1)
print(f"Total: {get_size(svmem.total)}")
time.sleep(0.1)
print(f"Available: {get_size(svmem.available)}")
time.sleep(0.1)
print(f"Used: {get_size(svmem.used)}")
time.sleep(0.1)
print(f"Percentage: {svmem.percent}%")
time.sleep(0.1)
print("="*40, "SWAP", "="*40)
time.sleep(0.1)
print(1)
swap = psutil.swap_memory()
time.sleep(0.1)
print(f"Total: {get_size(swap.total)}")
time.sleep(0.1)
print(f"Free: {get_size(swap.free)}")
time.sleep(0.1)
print(f"Used: {get_size(swap.used)}")
time.sleep(0.1)
print(f"Percentage: {swap.percent}%")
time.sleep(1)
#disk/storage
time.sleep(0.1)
print("="*40, "Disk Information", "="*40)
time.sleep(0.1)
print("Partitions and Usage:")
partitions = psutil.disk_partitions()
for partition in partitions:
    time.sleep(0.1)
    print(f"=== Device: {partition.device} ===")
    time.sleep(0.1)
    print(f"  Mountpoint: {partition.mountpoint}")
    time.sleep(0.1)
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    time.sleep(0.1)
    print(f"  Total Size: {get_size(partition_usage.total)}")
    time.sleep(0.1)
    print(f"  Used: {get_size(partition_usage.used)}")
    time.sleep(0.1)
    print(f"  Free: {get_size(partition_usage.free)}")
    time.sleep(0.1)
    print(f"  Percentage: {partition_usage.percent}%")
disk_io = psutil.disk_io_counters()
time.sleep(0.1)
print(f"Total read: {get_size(disk_io.read_bytes)}")
time.sleep(0.1)
print(f"Total write: {get_size(disk_io.write_bytes)}")
#NET
time.sleep(0.1)
print("="*40, "Network Information", "="*40)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        time.sleep(0.1)
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            time.sleep(0.1)
            print(f"  IP Address: {address.address}")
            time.sleep(0.1)
            print(f"  Netmask: {address.netmask}")
            time.sleep(0.1)
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            time.sleep(0.1)
            print(f"  MAC Address: {address.address}")
            time.sleep(0.1)
            print(f"  Netmask: {address.netmask}")
            time.sleep(0.1)
            print(f"  Broadcast MAC: {address.broadcast}")
#IO
net_io = psutil.net_io_counters()
time.sleep(0.1)
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
time.sleep(0.1)
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
