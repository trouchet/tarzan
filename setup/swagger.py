"""
This module sets up a Django Rest Framework (DRF) API documentation schema view using drf-yasg.

It defines an OpenAPI schema view for the "Tarzan API" with version 'v1'. The schema includes
information such as the API's title, description, contact information, and license details.

Attributes:
    schema_view (callable): A callable schema view configured with the specified API information.
        This view is accessible to the public and allows any user to access API documentation.

Example Usage:
    To access the API documentation, navigate to the schema view URL in your web browser.

    URL: http://your-api-url/swagger/
"""

# Import necessary modules
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create an OpenAPI schema view with the specified API information
SchemaView = get_schema_view(
    openapi.Info(
        title="Tarzan API",
        default_version="v1",
        description="Django API boilerplate",
        contact=openapi.Contact(email="brunolnetto@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
