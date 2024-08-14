#!/usr/bin/env python3
"""a class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """template for all authentication system to implement"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if the path is not in the
        list of strings excluded_paths:
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for ex_paths in excluded_paths:
            if excluded_paths[-1] != '/':
                excluded_paths == '/'
            if path == ex_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """validates all requests to secure the API"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns none - request will be a flask request obj"""
        return None
