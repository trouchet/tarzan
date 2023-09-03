import logging
import re

from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import CommonPasswordValidator

logger = logging.getLogger(__name__)

def validate_username(username):
    """
    Validates the given username against a regular expression pattern.
    
    Args:
        username (str): The username to be validated.

    Raises:
        ValidationError: If the username does not match the pattern.

    The username must be 150 characters or fewer and can only contain letters, digits, and the special characters @, ., +, -, and _.
    """
    pattern = r'^[\w.@+-]+$'
    
    if not re.match(pattern, username):
        raise ValidationError(
            "Username must be 150 characters or fewer. Letters, digits, and @/./+/-/_ only."
        )

def validate_password_similarity(password, user_info):
    """
    Validates the similarity of the given password to user-specific information.

    Args:
        password (str): The password to be validated.
        user_info (str): User-specific information to compare the password against.

    Raises:
        ValidationError: If the password is too similar to the user_info.
    """
    password_validation.validate_password(password, user_info)

def validate_password_length(password):
    """
    Validates the minimum length of the given password.

    Args:
        password (str): The password to be validated.

    Raises:
        ValidationError: If the password is shorter than 8 characters.
    """
    if len(password) < 8:
        raise ValidationError(
            "Your password must contain at least 8 characters."
        )

def validate_common_password(password):
    """
    Validates the given password against a list of common passwords.

    Args:
        password (str): The password to be validated.

    Raises:
        ValidationError: If the password is found in the list of common passwords.
    """
    validator = CommonPasswordValidator()
    validator.validate(password)

def validate_password_numeric(password):
    """
    Validates that the password is not entirely numeric.

    Args:
        password (str): The password to be validated.

    Raises:
        ValidationError: If the password is entirely numeric.
    """
    if password.isnumeric():
        raise ValidationError("Your password can't be entirely numeric.")