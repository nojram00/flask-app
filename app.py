from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

# from apscheduler.schedulers.background import BackgroundScheduler

from waitress import serve

from records import records as recs
from items import Items

from models.Items import items


def create_app():
    app = Flask(__name__)
    c = CORS(app)
    app.debug = True
    app.env = 'production'
    # app.config['ENV'] = 'production'

    #Sample Routes/Endpoints (Need ko lang pang reference)

    @app.route("/api/message")
    def test():
        return jsonify({'Message': 'I love you'}),200,{'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    #items

    @app.route('/api/getItems', methods=['GET'])
    def getItems():
        i = Items()
        r = i.itemsWithCategory()
        return jsonify(r), 200,{'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}


    @app.route('/api/addItems', methods=['POST'])
    def addItems():
        i = Items()
        name = request.args.post('name')
        price = request.args.post('price')
        quantity = request.args.post('quantity')
        category_index = request.args.post('categoryId')
        descrption = request.args.post('desc')

        r = i.insert(name=name, price=price, quantity=quantity, categoryId=category_index, description=descrption)
        return jsonify(r), 200, {'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8080)
    # serve(app, host='0.0.0.0', port=8080)
