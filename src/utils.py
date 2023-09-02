from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import CommonPasswordValidator

import logging
import re

logger = logging.getLogger(__name__)


def validate_username(username):
    # Define a regular expression pattern for allowed characters
    # Letters, digits, and the special characters @, ., +, -, and _
    pattern = r'^[\w.@+-]+$'

    # Use re.match() to check if the username matches the pattern
    if not re.match(pattern, username):
        raise ValidationError(
            "Username must be 150 characters or fewer. Letters, digits, and @/./+/-/_ only."
        )


def validate_password_similarity(password, user_info):
    # Check if the password is too similar to other personal information
    password_validation.validate_password(password, user_info)


def validate_password_length(password):
    if len(password) < 8:
        raise ValidationError(
            "Your password must contain at least 8 characters.")


def validate_common_password(password):
    validator = CommonPasswordValidator()
    validator.validate(password)


def validate_password_numeric(password):
    if password.isnumeric():
        raise ValidationError("Your password can't be entirely numeric.")
