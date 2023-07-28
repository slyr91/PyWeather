import time
from datetime import datetime

from flask import (
    Blueprint, render_template, request
)

import weather_icons
from api import location_api, weather_api

bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET'])
def index():
    client_ip = request.remote_addr
    print(client_ip)
    ip_info = location_api.get_ip_info(client_ip)
    print(ip_info)
    weather_info = weather_api.get_weather_info(ip_info['lat'], ip_info['lon'])
    package = packaged_weather_info(weather_info, ip_info)

    return render_template('app/index.html', today=package['today'], hourly=package['hourly'], daily=package['daily'])


def packaged_weather_info(weather_info, ip_info):
    current_hour = time.localtime().tm_hour

    weather_hours = []
    for i in range(current_hour + 24):
        datetime_str = datetime.strptime(weather_info['hourly']['time'][i], "%Y-%m-%dT%H:%M")
        hour = {'day': datetime_str.strftime("%#m/%#d"), 'time': datetime_str.strftime("%#I%p"),
                'temp': weather_info['hourly']['temperature_2m'][i],
                'apparent_temp': weather_info['hourly']['apparent_temperature'][i],
                'precipitation_prob': weather_info['hourly']['precipitation_probability'][i],
                'precipitation': weather_info['hourly']['precipitation'][i],
                'weather_code': weather_info['hourly']['weathercode'][i],
                'visibility': weather_info['hourly']['visibility'][i]}
        weather_hours.append(hour)

    weather_days = []
    for i in range(7):
        datetime_str = datetime.strptime(weather_info['daily']['time'][i], "%Y-%m-%d")
        day = {'day_of_week': datetime_str.strftime("%A"), 'date': datetime_str.strftime("%#m/%#d"),
               'weather_code': weather_info['daily']['weathercode'][i],
               'max_temp': weather_info['daily']['temperature_2m_max'][i],
               'min_temp': weather_info['daily']['temperature_2m_min'][i],
               'apparent_max_temp': weather_info['daily']['apparent_temperature_max'][i],
               'apparent_min_temp': weather_info['daily']['apparent_temperature_min'][i],
               'sunrise': weather_info['daily']['sunrise'][i], 'sunset': weather_info['daily']['sunset'][i],
               'uv_index_max': weather_info['daily']['uv_index_max'][i],
               'precipitation_sum': weather_info['daily']['precipitation_sum'][i],
               'rain_sum': weather_info['daily']['rain_sum'][i],
               'precipitation_probability_max': weather_info['daily']['precipitation_probability_max'][i],
               'windspeed_max': weather_info['daily']['windspeed_10m_max'][i],
               'windgusts_max': weather_info['daily']['windgusts_10m_max'][i],
               'winddirection_dominant': weather_info['daily']['winddirection_10m_dominant'][i]}
        weather_days.append(day)

    today = {'background_image': weather_icons.get_weather_url(weather_days[0]['weather_code']),
             'location': f"{ip_info['city']}, {ip_info['region']}",
             'icon_url': f"{weather_icons.get_icon_url(weather_days[0]['weather_code'])}",
             'classification': f"{weather_icons.get_code_classification(weather_days[0]['weather_code'])}",
             'current_temp': f"{weather_hours[current_hour]['temp']}",
             'apparent_temp': f"{weather_hours[current_hour]['apparent_temp']}",
             'max_temp': f"{weather_days[0]['max_temp']}", 'min_temp': f"{weather_days[0]['min_temp']}",
             'precipitation': f"{weather_days[0]['precipitation_probability_max']}"}

    hourly = []
    for i in range(current_hour + 1, current_hour + 24):
        a_hour = weather_hours[i]

        the_hour = {'background_image': weather_icons.get_weather_url(a_hour['weather_code']),
                    'time': a_hour['time'], 'icon_url': weather_icons.get_icon_url(a_hour['weather_code']),
                    'temp': a_hour['temp'], 'precipitation': a_hour['precipitation']}

        hourly.append(the_hour)

    daily = []
    for i in range(0, 7):
        a_day = weather_days[i]

        the_day = {'background_image': weather_icons.get_weather_url(a_day['weather_code']),
                   'day': a_day['day_of_week'], 'date': a_day['date'],
                   'icon_url': weather_icons.get_icon_url(a_day['weather_code']),
                   'classification': weather_icons.get_code_classification(a_day['weather_code']),
                   'max_temp': a_day['max_temp'], 'min_temp': a_day['min_temp'],
                   'precipitation': a_day['precipitation_probability_max']}

        daily.append(the_day)

    package = {'today': today, 'hourly': hourly, 'daily': daily}

    return package
