
from django.test import RequestFactory
from django.test import RequestFactory
from src.views import index, signup


def test_index_view():
    # Create an instance of the RequestFactory
    request_factory = RequestFactory()

    # Create an HTTP request (GET request in this case)
    request = request_factory.get("/")

    # Call the view function with the request
    response = index(request)

    # Perform assertions on the response

    # Check for a successful response status code
    assert response.status_code == 200


def test_signup_view_get():
    # Create an instance of the RequestFactory
    request_factory = RequestFactory()

    # Create a GET request to the signup view
    request = request_factory.get("/signup/")

    # Call the signup view function with the GET request
    response = signup(request)

    # Perform assertions on the response

    # Check for a successful response status code
    assert response.status_code == 200
