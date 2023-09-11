"""
Module Docstring:

This module provides fixtures for setting up test data.
"""

from src.middleware import RedirectMiddleware

redirect_middleware = RedirectMiddleware(get_response=None)
