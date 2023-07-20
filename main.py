from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page():
    return render_template('app/index.html')


if __name__ == '__main__':
    print("Hello")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
