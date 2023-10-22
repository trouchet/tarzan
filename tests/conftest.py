"""
Module Docstring:

This module provides fixtures for setting up test data.
"""

import pytest
from django.test import RequestFactory, Client
from src.middleware import RedirectMiddleware

redirect_middleware = RedirectMiddleware(get_response=None)


@pytest.fixture
def middleware():
    """
    Fixture for creating an instance of the RedirectMiddleware. This middleware is typically used
    to redirect requests to a specific URL or perform some processing. In this fixture, a lambda
    function is used to create a simple instance of the middleware that returns the string "42" as
    a placeholder response.

    Usage:
        You can use this fixture in your test cases to obtain an instance of the RedirectMiddleware.

    Example:
        middleware_instance = middleware()
    """
    return RedirectMiddleware(lambda request: "42")


@pytest.fixture
def client():
    """
    Fixture for creating an instance of the Django Client. The Client is a test client provided by
    Django for simulating HTTP requests. It allows you to send requests to your Django application
    and retrieve the responses for testing purposes.

    Usage:
        You can use this fixture in your test cases to obtain an instance of the Django Client.

    Example:
        test_client = client()
    """
    return Client()


@pytest.fixture
def request_factory():
    """
    Fixture for creating an instance of the Django RequestFactory. The RequestFactory is a utility
    for creating request objects, which can be used to simulate HTTP requests in Django test cases.
    This fixture is commonly used to create request objects for testing middleware and views.

    Usage:
        You can use this fixture in your test cases to obtain an instance of the RequestFactory.

    Example:
        request_factory = rf()
    """
    return RequestFactory()
