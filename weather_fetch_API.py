import location_fetch_API as where
import requests

def check_weather():
    if where.get_location() != None:
        r3 = requests.get("https://api.open-meteo.com/v1/gem?latitude=" + str(where.y["lat"]) + "&longitude=" + str(where.y["lon"]) + "&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,precipitation_hours,wind_speed_10m_max&timezone=America%2FNew_York&forecast_days=1")
        if r3.status_code == 200:
            return r3.text
        else:
            return None
    else:
        return None
    
print(check_weather())