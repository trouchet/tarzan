# pylint: disable=R0903
"""
Module: middleware.py

This module defines a custom middleware class, RedirectMiddleware, for handling invalid URLs
by redirecting to a default or specific URL.

Classes:
    - RedirectMiddleware: Middleware class for URL resolution and redirection.

"""

from django.urls import resolve, Resolver404
from django.http import HttpResponseRedirect


class RedirectMiddleware:
    """
    RedirectMiddleware Class

    Middleware class for handling invalid URLs by redirecting to a default or specific URL.

    Attributes:
        get_response (callable): The next middleware or view function in the request/response chain.

    Methods:
        __init__: Initializes the middleware with the get_response function.
        __call__: Handles the middleware logic to check and redirect invalid URLs.

    """

    def __init__(self, get_response, redirect_url='/api/'):
        """
        Initialize the middleware.

        Args:
            get_response (callable): The next middleware or view function in the
            request/response chain.

        """
        self.get_response = get_response
        self.redirect_url = redirect_url

    def __call__(self, request):
        """
        Handle the middleware logic to check and redirect invalid URLs.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponseRedirect: Redirects to a default or specific URL if the requested URL
            cannot be resolved.

        """
        # Get the URL path from the request
        path = request.path_info
        
        try:
            # Attempt to resolve the URL
            resolve(path)

        # pylint: disable=W0718
        except Resolver404:
            # If the URL cannot be resolved, it's invalid
            # Redirect to a default URL or a specific URL of your choice
            return HttpResponseRedirect(self.redirect_url)

        # Continue processing the request/response chain
        response = self.get_response(request)
            
        return response

