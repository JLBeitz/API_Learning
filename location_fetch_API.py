import requests
import json

def get_ip():
    r = requests.get("https://api.ipify.org")

    if r.status_code == 200:
        data = r.text
        return data
    else:
        return None
    
def get_location():
    if get_ip() != None:
        r2 = requests.get("http://ip-api.com/json/" + get_ip())
        if r2.status_code == 200:
            return r2.text
        else:
            return None
    else:
        return None

y = json.loads(get_location())