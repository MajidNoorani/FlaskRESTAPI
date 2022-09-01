#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:10:07 2022

@author: majid
"""

"""
designing the functions that were in app-1.py
"""
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
         'name': 'My Favorite Store',
         'items': [
             {
                 'name': 'My Item',
                 'Price': 15.99
                 }
             ]
         }
]

# POST - used to recieve data
# GET -  used to send data back only

# End points design:
@app.route('/')
def home():
    return render_template('index.html')

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    # we are creating an empty store
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
        }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>') #http://127.0.0.1:5000/store/some_name
def get_store(name):
    # find a store
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores" : stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'Price': request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})
# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') 
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
print('done')