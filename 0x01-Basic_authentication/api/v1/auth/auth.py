#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """ Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if the path is not in the
        list of strings excluded_paths"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # add a trailing slash to path if it doesn't have one
        if path[-1] != '/':
            path += '/'

        # normalize excluded_paths:
        excluded_paths = [p + '/' if p[-1] != '/'
                          else p for p in excluded_paths]
        # check for wildcard matching
        for pattern in excluded_paths:
            if fnmatch.fnmatch(path, pattern):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the flask request object"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object """
        return None
