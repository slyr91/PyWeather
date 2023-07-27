from flask import Flask, render_template
from os import environ

import index
from api import location_api

app = Flask(__name__)

app.register_blueprint(index.bp)


# @app.route("/")
def page():
    location = location_api.get_ip_info("23.43.12.1")
    print(location['lat'])
    return render_template('app/index.html')


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(index.bp)

    port = environ.get('PORT', 8080)
    host = '127.0.0.1' if port == 8080 else '0.0.0.0'
    app.run(host=host, port=port, debug=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
