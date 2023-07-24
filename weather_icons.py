
def weather_icon_file_from_code(code: int):
    match code:
        case 0:
            return "static/icons/sunny.png"
        case 1 | 2 | 3:
            return "static/icons/cloud-covered-sun.png"
        case 45 | 48:
            return "static/icons/fog.png"
        case 51 | 53 | 55 | 56 | 57 | 80 | 81 | 82:
            return "static/icons/sun-and-rain.png"
        case 61 | 63 | 65 | 66 | 67:
            return "static/icons/rain.png"
        case 71 | 73 | 75 | 77:
            return "static/icons/snow.png"
        case 71 | 73 | 75 | 77:
            return "static/icons/snow.png"
        case 85, 86:
            return "static/icons/sun-and-snow.png"
        case 95:
            return "static/icons/thunderstorm.png"
        case 96 | 99:
            return "static/icons/thunder-and-hail.png"

# TODO create a method to get the url for the static icon