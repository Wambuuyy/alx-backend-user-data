#!/usr/bin/env python3
"""basic authorization"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    empty for now
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the base64 part of authorization header
        for a basic authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
