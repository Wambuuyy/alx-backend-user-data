#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()

""" Retreive this user via the class BasicAuth """

ba = BasicAuth()
    res = ba.user_object_from_credentials("u1@gmail.com", "pwd")
    if res is not None:
        print("user_object_from_credentials must return None if 'user_email' is not linked to any user")
        exit(1)
    
    print("OK", end="")