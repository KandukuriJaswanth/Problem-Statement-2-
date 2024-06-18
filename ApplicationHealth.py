import requests
import logging

# Set up logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Application URL
APP_URL = 'http://your_application_url_here'

def check_application_health():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            message = "Application is up and running."
        else:
            message = f"Application is down. Status code: {response.status_code}"
        logging.info(message)
        print(message)
    except requests.exceptions.RequestException as e:
        message = f"Application is down. Error: {e}"
        logging.error(message)
        print(message)

if __name__ == "__main__":
    check_application_health()
