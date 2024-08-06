#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns false - path and excluded_paths will be used later """
        return False

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object """
        return None
