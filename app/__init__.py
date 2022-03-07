import os
from flask import Flask, request, jsonify
from app.products import get_products, get_product, create_product, update_product, delete_product
import json

app=Flask(__name__)

FILEPATH = os.getenv("FILEPATH")

@app.get('/products')
def product_list():
    page = request.args.get("page")
    if page == None:
        page = 1
    per_page = request.args.get("per_page")
    if per_page == None:
        per_page = 3
    response = get_products(FILEPATH, page, per_page)
    return jsonify(response), 200

@app.get('/products/<product_id>')
def product(product_id):
    try:
        product = get_product(FILEPATH, product_id)
        return jsonify(product), 200
    except UnboundLocalError:
        return {'error': f'product id {product_id} not found'}, 404

@app.post('/products')
def create():
    data = request.data
    item = create_product(FILEPATH, json.loads(data))
    return item, 201

@app.patch('/products/<product_id>')
def patch(product_id):
    try:
        data = request.data
        updated_product = update_product(FILEPATH, json.loads(data), product_id)
        return updated_product
    except UnboundLocalError:
        return {'error': f'product id {product_id} not found'}, 404


@app.delete('/products/<product_id>')
def delete(product_id):
    try:
        popped_product = delete_product(FILEPATH, product_id)
        return popped_product
    except UnboundLocalError:
        return {'error': f'product id {product_id} not found'}, 404
