from flask import (
    Blueprint, render_template, request
)

from api import location_api, weather_api

bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET'])
def index():
    client_ip = request.remote_addr
    ip_info = location_api.get_ip_info(client_ip)
    weather_info = weather_api.get_weather_info(ip_info['lat'], ip_info['lon'])
    package = packaged_weather_info(weather_info, ip_info)

    return render_template('app/index.html')

# TODO finish the package method.
def packaged_weather_info(weather_info, ip_info):
    daily = { 'location': f"{ip_info['city']}, {ip_info['region']}",  }
