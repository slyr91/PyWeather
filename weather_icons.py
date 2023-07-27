from flask import url_for


def weather_icon_file_from_code(code: int):
    match code:
        case 0:
            return "icons/sunny.png"
        case 1 | 2 | 3:
            return "icons/cloud-covered-sun.png"
        case 45 | 48:
            return "icons/fog.png"
        case 51 | 53 | 55 | 56 | 57 | 80 | 81 | 82:
            return "icons/sun-and-rain.png"
        case 61 | 63 | 65 | 66 | 67:
            return "icons/rain.png"
        case 71 | 73 | 75 | 77:
            return "icons/snow.png"
        case 85, 86:
            return "icons/sun-and-snow.png"
        case 95:
            return "icons/thunderstorm.png"
        case 96 | 99:
            return "icons/thunder-and-hail.png"


def get_icon_url(code: int):
    return url_for('static', filename=weather_icon_file_from_code(code))


def get_code_classification(code: int):
    match code:
        case 0:
            return "Sunny"
        case 1 | 2 | 3:
            return "Cloudy"
        case 45 | 48:
            return "Fog"
        case 51 | 53 | 55 | 56 | 57 | 80 | 81 | 82:
            return "Showers"
        case 61 | 63 | 65 | 66 | 67:
            return "Rain"
        case 71 | 73 | 75 | 77:
            return "Snow"
        case 85, 86:
            return "Snow Flurry"
        case 95:
            return "Thunderstorm"
        case 96 | 99:
            return "Thunder and Hail"


def get_weather_image_from_code(code: int):
    match code:
        case 0:
            return "images/sunny.jpg"
        case 1 | 2 | 3:
            return "images/cloud-covered-sun.jpg"
        case 45 | 48:
            return "images/fog.jpg"
        case 51 | 53 | 55 | 56 | 57 | 80 | 81 | 82:
            return "images/sun-and-rain.jpg"
        case 61 | 63 | 65 | 66 | 67:
            return "images/rain.jpg"
        case 71 | 73 | 75 | 77:
            return "images/snow.jpg"
        case 85, 86:
            return "images/sun-and-snow.jpg"
        case 95:
            return "images/thunderstorm.jpg"
        case 96 | 99:
            return "images/thunder-and-hail.jpg"


def get_weather_url(code: int):
    return url_for('static', filename=get_weather_image_from_code(code))
