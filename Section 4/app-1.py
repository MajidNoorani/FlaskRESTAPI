#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:29:56 2022

@author: majid
"""
"""
setting up endpoints with flask_restful
"""
from flask import Flask, request
from flask_restful import Resource, Api 
# if our API is concerened with pianos, resource can be a piano
# if our API is concerened with students, resource can be a student

app = Flask(__name__)
api = Api(app)

items= []

# every resource has to be a class

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:        
                return item
        return {'item': None}, 404 # 404 is the error code: 404 not found
    
    def post(self, name): # for post still we get name in the request(url)
        data = request.get_json(force=False, silent=False) 
        # force=True means you dont need Content-type header
        # silent=True means that dont retrn error, just return None
        new_item = {'name': name,'price': data['price']}
        items.append(new_item)
        return new_item, 201
    
class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True) # debug makes flask to return nice errors it any error had been raised 