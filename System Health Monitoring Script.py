import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 200  # number of processes

def log_alert(message):
    logging.info(message)
    print(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High Memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"High Disk usage detected: {disk_usage}%")

def check_running_processes():
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        log_alert(f"High number of running processes detected: {processes}")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
