"""
This module contains unit tests for utility functions related to user validation.

It includes test cases for various utility functions defined in the 'src.utils' module,
such as username validation, password similarity, password length, common password checks,
and numeric password checks. These tests ensure that the utility functions perform as
expected and validate user inputs correctly.

Attributes:
    (No module-level attributes)

Description:
    The test cases in this module are designed to validate the behavior of utility functions
    that are used for user input validation. These functions are critical for enforcing
    security and data quality standards in the application.

Usage:
    To run these tests, you can use the pytest framework. Simply execute the pytest command
    in the terminal while in the project directory:

    ```
    pytest test_utils.py
    ```

    The test cases will be executed, and any assertion failures or errors will be reported.
    Ensure that the 'src.utils' module is correctly imported and that the utility functions
    in 'src.utils' are implemented and functioning as intended.
"""

from django.core.exceptions import ValidationError
import pytest

from src.utils import (
    validate_username,
    validate_password_similarity,
    validate_password_length,
    validate_common_password,
    validate_password_numeric,
)


def test_validate_username_valid():
    """
    Test valid usernames using the validate_username function.

    This test case checks that the validate_username function correctly accepts
    valid usernames, including usernames with letters, numbers, dots, at symbols,
    hyphens, and plus signs. It asserts that no ValidationError is raised for
    valid usernames.
    """

    # Valid usernames
    valid_usernames = ["user123", "user.name",
                       "user@domain.com", "user-123", "user+test"]
    for username in valid_usernames:
        assert validate_username(username) is None


def test_validate_username_invalid():
    """
    Test invalid usernames using the validate_username function.

    This test case checks that the validate_username function correctly raises
    a ValidationError for invalid usernames, including usernames with special
    characters such as '$', '!', '&', '/', and '*'.
    """

    # Invalid usernames
    invalid_usernames = ["user$", "user!",
                         "user&test!", "user/test", "user*test"]
    for username in invalid_usernames:
        with pytest.raises(ValidationError):
            validate_username(username)


def test_validate_password_similarity():
    """
    Test password similarity using the validate_password_similarity function.

    This test case checks that the validate_password_similarity function correctly
    raises a ValidationError when the password is too similar to user information.
    It compares the password "Password123" to the user information "Password123"
    and asserts that a ValidationError is raised.
    """

    # Password similarity should raise ValidationError
    password = "Password123"
    user_info = "Password123"
    with pytest.raises(ValidationError):
        validate_password_similarity(password, user_info)


def test_validate_password_length_valid():
    """
    Test valid password length using the validate_password_length function.

    This test case checks that the validate_password_length function correctly
    accepts valid passwords with lengths of 8 characters and more. It asserts
    that no ValidationError is raised for valid passwords.
    """

    # Valid password length
    valid_passwords = ["Pass1234", "LongerPass12345"]
    for password in valid_passwords:
        assert validate_password_length(password) is None


def test_validate_password_length_invalid():
    """
    Test invalid password length using the validate_password_length function.

    This test case checks that the validate_password_length function correctly
    raises a ValidationError for invalid passwords with lengths less than 8
    characters, such as "Short" and "1234567".
    """

    # Invalid password length
    invalid_passwords = ["Short", "1234567"]
    for password in invalid_passwords:
        with pytest.raises(ValidationError):
            validate_password_length(password)


def test_validate_common_password():
    """
    Test common passwords using the validate_common_password function.

    This test case checks that the validate_common_password function correctly
    raises a ValidationError for common passwords such as "password", "admin123",
    and "letmein".
    """

    # Common passwords should raise ValidationError
    common_passwords = ["password", "admin123", "letmein"]
    for password in common_passwords:
        with pytest.raises(ValidationError):
            validate_common_password(password)


def test_validate_password_numeric():
    """
    Test numeric passwords using the validate_password_numeric function.

    This test case checks that the validate_password_numeric function correctly
    raises a ValidationError for passwords consisting entirely of numeric digits,
    such as "123456", "0000", and "987654321".
    """

    # Numeric passwords should raise ValidationError
    numeric_passwords = ["123456", "0000", "987654321"]
    for password in numeric_passwords:
        with pytest.raises(ValidationError):
            validate_password_numeric(password)
