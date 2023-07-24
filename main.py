from flask import Flask, render_template
from api import location_api

app = Flask(__name__)


@app.route("/")
def page():
    location = location_api.get_ip_info("23.43.12.1")
    print(location['lat'])
    return render_template('app/index.html')


if __name__ == '__main__':
    print("Hello")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
