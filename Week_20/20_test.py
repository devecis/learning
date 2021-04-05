import requests
import json
import datetime
import time

for i in range(10):
    iss_data = requests.get("http://api.open-notify.org/iss-now.json")
    packages_json = iss_data.json()
    results = []

    time_samp = packages_json["timestamp"]
    lat_samp = packages_json["iss_position"]["latitude"]
    long_samp = packages_json["iss_position"]["longitude"]
    con_samp = datetime.datetime.fromtimestamp(time_samp)
    t_samp = con_samp.strftime("%Y-%b-%d %H:%M:%S")
    data = {"Timestamp": t_samp, "Latitude": lat_samp, "Longitude": long_samp}

    results.append(data)
    with open("output_iss.json", "a") as f:
        json.dump(results, f, indent=2)
    time.sleep(2)
    # print(con_samp.strftime('%Y-%b-%d %H:%M:%S'))
    # print(lat_samp)
    # print(long_samp)
