#!/usr/bin/env python3
"""a class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """template for all authentication system to implement"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns false - path and excluded paths be used later"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """returns None -request will be the flask request obj"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """returns none - request will be a flask request obj"""
        return None
