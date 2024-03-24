from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
import graphene
import requests
from flask_restful import reqparse
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

class GetProducts(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.products
        collection = db.product_data
        results = dumps(collection.find())
        return json.loads(results)

api.add_resource(GetProducts, '/getProducts')

class Product(graphene.ObjectType):
    title = graphene.String()

# Mapping values to Products
class Query(graphene.ObjectType):
    product = graphene.List(Product)

    def resolve_product(root, info):
        data = requests.get('http://127.0.0.1:5000/getProducts')
        json_content = json.loads(data.text)
        
        # Extracting titles from all documents
        titles = [item.get('Title') for item in json_content]
        
        # Creating a list of Product objects
        products = [Product(title=title) for title in titles]
        
        return products

class GetTitles(Resource):
    def get(self):
        schema = graphene.Schema(query=Query)
        query = """
                {
                product {
                title
                }
                }
        """

        # Execute the GraphQL query
        result = schema.execute(query)
        
        # Return the data as JSON
        return result.data

api.add_resource(GetTitles, '/getTitles')

class InsertProduct(Resource):
    # Define your custom API key
    CUSTOM_API_KEY = "custom_api_key"

    def post(self):
        # Check if the API key is provided in the URL
        api_key = request.args.get('api_key')
        if api_key != self.CUSTOM_API_KEY:
            return {"error": "Unauthorized. Please provide a valid API key."}, 401
        
        # Parse the request data
        data = request.get_json()
        
        # Extract data from the request
        product_id = data.get('ProductId')
        title = data.get('Title')
        price = data.get('Price')
        quantity = data.get('Quantity')
        
        # Validate the request data
        if not all([product_id, title, price, quantity]):
            return {"error": "Missing required data"}, 400
        
        # Connect to MongoDB and insert the product data
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.products
        collection = db.product_data
        
        new_record = {"ProductId": product_id, "Title": title, "Price": price, "Quantity": quantity}
        collection.insert_one(new_record)
        
        return {"status": "inserted"}, 201
api.add_resource(InsertProduct, '/insertProduct')

class APIDescription(Resource):
    def get(self):
        description = {
            "/getProducts": "GET request to retrieve a list of all products from the mongo database.",
            "/getTitles": "GET request to retrieve titles of all products using GraphQL query.",
            "/insertProduct?api_key=<YOUR_API_KEY>": "POST request to insert a new product into the database. Requires a valid API key.",
            "/": "Description page containing a list of the API URLs that are available and a brief description of how they work."
        }
        return jsonify(description)

api.add_resource(APIDescription, '/')

if __name__ == '__main__':
    app.run(debug=False)