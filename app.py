from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from apscheduler.schedulers.background import BackgroundScheduler

from waitress import serve

from records import records as recs
from items import items


def create_app():
    app = Flask(__name__)
    c = CORS(app)
    app.debug = True
    app.env = 'production'
    # app.config['ENV'] = 'production'

    #Sample Routes/Endpoints (Need ko lang pang reference)

    @app.route("/")
    def test():
        return jsonify({'Message': 'I love you'}),200,{'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    @app.route('/addNewData', methods=['POST'])
    def add():
        r = recs()
        fname = request.args.get('fname')
        lname = request.args.get('lname')
        age = request.args.get('age')

        data = r.insertNewData(fname, lname, age)

        return jsonify({'message': data}), 200, {'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}

    @app.route('/getDataById', methods=['GET'])
    def dataById():
        r = recs()
        id = request.args.get('id')

        # print(id)
        if id == None:
            raise ValueError('The ID you entered is null')
            return jsonify({'error':'null value'}), 200, {'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}

        data = r.getDataById(id)

        if len(data) == 0:
            print('Empty data')
            return jsonify({'message':'Empty data, no data fetched.'})

        return jsonify(data),200, {'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}


    @app.route('/getAllData', methods=['GET'])
    def allData():
        r = recs()
        data = r.getData()
        # print(data)
        return jsonify(data), 200, {'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}

    #items

    @app.route('/getItems', methods=['GET'])
    def allItems():
        i = items()
        category = request.args.get('category')
        print(category)

        if category:
            # Categories:
            # ram
            # motherboards
            # hardrives
            # monitors
            # case
            # cpu
            # fan
            data = items.fetch_items_by_category(category)
        else:
            data = i.retrieve()

        return jsonify(data), 200, {'Content-Type': 'application/json', "Access-Control-Allow-Origin": '*'}

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8080)
    # serve(app, host='0.0.0.0', port=8080)
