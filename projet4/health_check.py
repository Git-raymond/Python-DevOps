# health_check.py

import psutil

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

def check_memory():
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}%")

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    print(f"Disk Space Usage: {disk_info.percent}%")

if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk_space()
