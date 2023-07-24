import requests


# the returned object is a dictionary with the following keys:
# status, lat, lon
def get_ip_info(ip: str):
    if(ip.startswith("192.168")):
        response = requests.get(f"http://ip-api.com/json/8.8.8.8?fields=61439")
    else:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=61439")
    return response.json()
