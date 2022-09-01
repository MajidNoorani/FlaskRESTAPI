#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:35:19 2022

@author: majid
"""
"""
making our code a bit more nicer (using filters)
"""
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
# if our API is concerened with pianos, resource can be a piano
# if our API is concerened with students, resource can be a student

app = Flask(__name__)
app.secret_key = 'Majid'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth (creates this endpoint) 

items= []

# every resource has to be a class

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # next returns the first item that matches
        # if nothing matches it will return None
        item = next(filter(lambda x: x['name'] == name, items), None) 
        return {'item': item}, 200 if item else 404
    
    def post(self, name): # for post still we get name in the request(url)
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message: An item with name {} already exists.'.format(name)}, 400
        
        data = request.get_json() 
        new_item = {'name': name,'price': data['price']}
        items.append(new_item)
        return new_item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}
    
    def put(self, name):
        # to set which kind of data can pass and which type and features it shpuld have, we uses parser
        # we use this parser specially for the update line in the following and we dont want the
        # client to chage the name of the items
        # required=True means that the input needs to have this key
        parser = reqparse.RequestParser()
        parser.add_argument('price', 
                            type=float,
                            required=True,
                            help='price field cannot be left blank. spelling might be wrong'
                            )
        
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
    
class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True) # debug makes flask to return nice errors if any error had been raised 
