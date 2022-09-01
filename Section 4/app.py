#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:45:31 2022

@author: majid
"""
"""
just a preface of the flask_restful and see how it works
"""
from flask import Flask
from flask_restful import Resource, Api 
# if our API is concerened with pianos, resource can be a piano
# if our API is concerened with students, resource can be a student

app = Flask(__name__)
api = Api(app)

# every resource has to be a class

class Student(Resource):
    def get(self, name):
        return {'student': name}
    
api.add_resource(Student, '/student/<string:name>') # http;//127.0.0.1:5000/student/Rolf

app.run(port=5000)