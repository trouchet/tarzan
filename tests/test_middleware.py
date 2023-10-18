import pytest
from django.test import RequestFactory, Client
from src.middleware import RedirectMiddleware


@pytest.fixture
def middleware():
    return RedirectMiddleware(lambda request: "42")


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def rf():
    return RequestFactory()


redirect_url = "/api/"
valid_url = "/api/"
invalid_url = "/invalid/"


def test_valid_url(middleware, rf):
    # Test a valid URL should not be redirected
    request = rf.get(valid_url)
    response = middleware(request)
    assert response == "42"


def test_middleware_in_integration(client):
    # Test the middleware in an integration scenario
    response = client.get(invalid_url)

    # Should be redirected
    assert response.status_code == 302

    # Should be redirected to the default URL
    assert response.url == redirect_url
