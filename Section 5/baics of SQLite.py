#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:41:46 2022

@author: majid
"""

"""
This code reminds us about the syntax of SQLite package 
The target is make a table of users to use it for sign up 
"""

import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password txt)"
cursor.execute(create_table)

user = (1, 'Majid', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)  

users = [
    (1, "Majid", "asdf"),
    (2, "Ahmad", "qwer")
    ]
cursor.executemany(insert_query, users)
select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)
    
connection.commit()
connection.close()