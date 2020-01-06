import json
import time

import requests

while True:
    response = requests.get('http://104.248.83.114:8080/location.get')
    time.sleep(5*60)
    data = response.json()
    print(data)
