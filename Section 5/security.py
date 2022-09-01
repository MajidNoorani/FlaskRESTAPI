#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:44:48 2022

@author: majid
"""
"""
this is created to identify the users to see 
whether they logged in with right pass or not 
"""

from hmac import compare_digest
from user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)