#!/usr/bin/env python3
"""session auth class"""
from api.v1.auth.auth import Auth
import uuid
import os
from typing import Dict
from models.user import User
from flask import request


class SessionAuth(Auth):
    """session authentication class inheriting from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session id and returns accordingly"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user ID based on a session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def session_cookie(self, request) -> str:
        """Returns the session cookie from the request."""
        return request.cookies.get(os.getenv('SESSION_NAME'))

    def authorization_header(self, request) -> str:
        """Returns the authorization header from the request."""
        return request.headers.get('Authorization')

    def current_user(self, request) -> str:
        """Returns the User ID based on the request."""
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
