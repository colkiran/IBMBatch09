import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'item': '2 ltr Bottle', 'price': 120, 'qty': 75},
    'coke': {'item': '500 ml Bootle', 'price': 60, 'qty': 100},
    'thumbs_up':{'item': '300 ML can', 'price': 80, 'qty': 50}
}

class Product(Resource):

    def get(self, product):
        return {product :products[product]}

    def put(self, product):
        products[product]['cat'] = request.form['cat']
        return {product: products[product]}

    def patch(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product][list(data.keys())[0]] = data[list(data.keys())[0]]
        return {product: products[product]}

    def post(self, product):
        data1 = request.json
        data = json.loads(data1)
        products[product] = data
        return products

    def delete(self, product):
        if product in products:
            del products[product]
            return products
        else:
            return {'KeyError': "Please enter a valid key....."}

api.add_resource(Product, "/getproduct/<string:product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)