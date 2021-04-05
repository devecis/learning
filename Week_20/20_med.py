import requests
import json
import datetime
import time
from os import system

for i in range(10):
    iss_data = requests.get('http://api.open-notify.org/iss-now.json')
    packages_json = iss_data.json()
    time_samp = packages_json['timestamp']
    lat_samp = packages_json['iss_position']['latitude']
    long_samp = packages_json['iss_position']['longitude']
    packages_str = json.dumps(packages_json, indent=2)
    con_samp = datetime.datetime.fromtimestamp(time_samp)
    print('Timestamp: ' + con_samp.strftime('%Y-%b-%d %H:%M:%S'))
    print('Latitude: ' + lat_samp)
    print('Longitude: ' + long_samp)
    time.sleep(2)
    system('clear')