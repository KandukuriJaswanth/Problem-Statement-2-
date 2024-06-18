from flask import Flask, jsonify, render_template
import psutil
import logging
import os

# Initialize Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds for system health checks
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 200  # number of processes

# Path to local application file to check
APP_FILE_PATH = 'D:/B.TECH/Mini Project/QA/por/po/index.html'  # Replace with your actual file path

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

def check_application_health():
    if os.path.exists(APP_FILE_PATH):
        message = "Application is up and running."
        logging.info(message)
        print(message)
    else:
        message = "Application file not found."
        logging.error(message)
        print(message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/system_health', methods=['GET'])
def get_system_health():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
 
    return jsonify(message="System health checks completed."), 200

@app.route('/api/application_health', methods=['GET'])
def get_application_health():
    check_application_health()
    
    return jsonify(message="Application health check completed."), 200

if __name__ == '__main__':
    app.run(debug=True)
