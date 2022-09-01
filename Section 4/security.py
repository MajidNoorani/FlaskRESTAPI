#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:17:15 2022

@author: majid
"""
    # compare_digest and safe_str_cmp are for comparing 2 objects 
    # without being woried about different versions and other possible problems
from hmac import compare_digest
#from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password):
        return user

def identity(payload): 
    # identity is unique for JWT
    # payload is the content of JWT token
    user_id = payload['identity']
    return userid_table.get(user_id, None)