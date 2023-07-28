from flask import Flask
from os import environ

import index


def create_app():
    appf = Flask(__name__)
    appf.register_blueprint(index.bp)

    return appf


if __name__ == '__main__':
    app = create_app()
    port = environ.get('PORT', 8080)
    host = '127.0.0.1' if port == 8080 else '0.0.0.0'
    app.run(host=host, port=port, debug=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
