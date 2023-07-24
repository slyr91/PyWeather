import requests

def get_weather_info(lat: str, lon: str):
    weather_info = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly"
                                f"=temperature_2m,apparent_temperature,precipitation_probability,precipitation,"
                                f"weathercode,visibility&daily=weathercode,temperature_2m_max,temperature_2m_min,"
                                f"apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max,"
                                f"precipitation_sum,rain_sum,precipitation_probability_max,windspeed_10m_max,"
                                f"windgusts_10m_max,"
                                f"winddirection_10m_dominant&temperature_unit=fahrenheit&windspeed_unit=mph"
                                f"&precipitation_unit=inch&timezone=auto")
    return weather_info.json()