"""
Test module for src.views.
"""
from src.views import index, signup


def test_index_view(request_factory):
    """
    Test the index view with a GET request.

    Args:
    request_factory: A factory for creating HTTP requests.

    Asserts:
    - The response status code is 200 (OK).
    """

    # Create an HTTP request (GET request in this case)
    request = request_factory.get('/')

    # Call the view function with the request
    response = index(request)

    # Perform assertions on the response

    # Check for a successful response status code
    assert response.status_code == 200


def test_signup_view_get(request_factory):
    """
    Test the signup view with a GET request.

    Args:
    request_factory: A factory for creating HTTP requests.

    Asserts:
    - The response status code is 200 (OK).
    """
    
    # Create a GET request to the signup view
    request = request_factory.get('/signup/')

    # Call the signup view function with the GET request
    response = signup(request)

    # Perform assertions on the response

    # Check for a successful response status code
    assert response.status_code == 200
