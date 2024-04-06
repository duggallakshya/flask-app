from flask import Blueprint, jsonify, request
import json

product_bp = Blueprint('product_bp', __name__)

# Logic to fetch all products
def get_all_products():
    with open('products.json', 'r') as file:
        products = json.load(file)
    return products

# Logic to add a new product
def add_product(product_data):
    with open('products.json', 'r') as file:
        products = json.load(file)
    
    products.append(product_data)
    
    with open('products.json', 'w') as file:
        json.dump(products, file)

@product_bp.route('/all-products', methods=['GET'])
def all_products():
    products = get_all_products()
    return jsonify(products)

@product_bp.route('/add-product', methods=['POST'])
def add_new_product():
    product_data = request.get_json()
    add_product(product_data)
    return jsonify({"message": "Product added successfully"})
