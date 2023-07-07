from flask import Flask

app = Flask(__name__)


@app.route("/gago")
def gago():
    return 'gago!'

@app.route('/kupal')
def kupal():
    return 'kupal ka'

@app.route('/')
def tangina_mo():
    return 'tangina mo!'


if __name__ == '__main__':
    app.run(debug=True)
