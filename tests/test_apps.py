"""
Module Docstring:

This module contains a test function to check attributes of a Django app config instance.

"""

from django.apps import apps


def test_app_config_attributes():
    """
    Test function to check attributes of a Django app config instance.

    This function retrieves the app config instance for the 'src' app and checks
    two of its attributes: 'default_auto_field' and 'name'.

    Raises:
        AssertionError: If the attributes do not match the expected values.

    """
    # Get the app config instance
    app_config = apps.get_app_config("src")

    # Check the attributes
    assert app_config.default_auto_field == "django.db.models.BigAutoField"
    assert app_config.name == "src"
