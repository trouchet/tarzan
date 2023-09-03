import pytest
from django.core.exceptions import ValidationError
from src.utils import (
    validate_username,
    validate_password_similarity,
    validate_password_length,
    validate_common_password,
    validate_password_numeric,
)

def test_validate_username_valid():
    # Valid usernames
    valid_usernames = ["user123", "user.name", "user@domain.com", "user-123", "user+test"]
    for username in valid_usernames:
        assert validate_username(username) is None

def test_validate_username_invalid():
    # Invalid usernames
    invalid_usernames = ["user$", "user!", "user&test!", "user/test", "user*test"]
    for username in invalid_usernames:
        with pytest.raises(ValidationError):
            validate_username(username)

def test_validate_password_similarity():
    # Password similarity should raise ValidationError
    password = "Password123"
    user_info = "Password123"
    with pytest.raises(ValidationError):
        validate_password_similarity(password, user_info)

def test_validate_password_length_valid():
    # Valid password length
    valid_passwords = ["Pass1234", "LongerPass12345"]
    for password in valid_passwords:
        assert validate_password_length(password) is None

def test_validate_password_length_invalid():
    # Invalid password length
    invalid_passwords = ["Short", "1234567"]
    for password in invalid_passwords:
        with pytest.raises(ValidationError):
            validate_password_length(password)

def test_validate_common_password():
    # Common passwords should raise ValidationError
    common_passwords = ["password", "admin123", "letmein"]
    for password in common_passwords:
        with pytest.raises(ValidationError):
            validate_common_password(password)

def test_validate_password_numeric():
    # Numeric passwords should raise ValidationError
    numeric_passwords = ["123456", "0000", "987654321"]
    for password in numeric_passwords:
        with pytest.raises(ValidationError):
            validate_password_numeric(password)