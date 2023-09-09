# pylint: disable=R0903
"""
This module defines custom forms for user registration and authentication.

It includes a `CustomUserCreationForm` class, a subclass of Django's built-in `UserCreationForm`,
with additional customizations for user registration. The form fields are defined using the
`getTypeField` function, which generates form fields with customizable attributes.

Attributes:
    CustomUserCreationForm (class): A custom user registration form that inherits from
        Django's `UserCreationForm`. It includes fields for username, password, first name,
        last name, and email, with various customizations, such as password validation.

    getTypeField (function): A utility function to generate form fields of different types
        (e.g., CharField, EmailField) with customizable attributes like max length, required,
        label, input type, and validators.

    password_validators (list): A list of custom password validation functions, including checks
        for password similarity, length, common passwords, and numeric content.

Description:
    This module provides a flexible and extensible way to create custom user registration forms
    in a Django application. The `CustomUserCreationForm` class allows developers to easily
    customize the registration form fields and validation rules to suit their application's
    requirements.

Usage:
    To use these forms in your Django application, you can import them into your views or other
    parts of your application. For example, in a view that handles user registration:

    ```python
    from .forms import CustomUserCreationForm

    def register_user(request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                # Process the form data and create a new user
                # ...
        else:
            form = CustomUserCreationForm()

        return render(request, 'registration/register.html', {'form': form})
    ```

    This module provides a convenient way to create customized user registration forms
    with a range of options for customization.
"""

from django.forms import CharField, \
    EmailField, \
    PasswordInput, \
    ValidationError, \
    TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from . import utils


def label_input(text, is_required):
    """
    Generate Label Text

    Generates a label with an asterisk (*) if the field is required.

    Args:
        text (str): The label text.
        is_required (bool): Indicates whether the field is required.

    Returns:
        str: The formatted label text.

    """

    if is_required:
        label_text = f'{text}*'
    else:
        label_text = text
    return label_text

def build_widget_config(label, is_required):
    """
    Build Widget Configuration

    Builds a widget configuration dictionary with a placeholder and CSS class.

    Args:
        label (str): The label text.
        is_required (bool): Indicates whether the field is required.

    Returns:
        dict: A dictionary containing widget configuration options.

    """

    return {
        'placeholder': label_input(label, is_required),
        'class': 'form-control',
    }

# pylint: disable=R0913
def get_type_field(
        type_field,
        max_length_value,
        is_required,
        label,
        input_type,
        validators_list):
    """
    Create Form Field

    Creates a form field of a specified type with a custom label, widget, and validators.

    Args:
        type_field (class): The type of form field to create (e.g., CharField, EmailField, etc.).
        max_length_value (int): The maximum length allowed for the field.
        is_required (bool): Indicates whether the field is required.
        label (str): The label text for the field.
        input_type (class): The type of input widget to use (e.g., TextInput, EmailInput, etc.).
        validators_list (list): A list of validation functions to apply to the field.

    Returns:
        type_field: A form field instance with the specified configuration.

    """

    widget_config = build_widget_config(label, is_required)

    return type_field(
        max_length=max_length_value,
        required=is_required,
        widget=input_type(attrs=widget_config),
        validators=validators_list,
    )

password_validators = [
    password_validation.validate_password,  # Password similarity check
    utils.validate_password_length,         # Password length check
    utils.validate_common_password,         # Commonly used password check
    utils.validate_password_numeric,        # Numeric check
]

# pylint: disable=R0901
class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form extending Django's built-in UserCreationForm.

    This form provides customizations for user registration fields, including username,
    password, first name, last name, and email. It also includes additional password
    validation rules.

    Attributes:
        username (CharField): The username field with a maximum length of 150 characters.
        password (CharField): The password field with a maximum length of 150 characters.
        first_name (CharField): The first name field with a maximum length of 30 characters.
        last_name (CharField): The last name field with a maximum length of 30 characters.
        email (EmailField): The email field with a maximum length of 254 characters.

    Methods:
        __init__(self, *args, **kwargs): Initializes the form, customizing the help text
            for the password field.

        clean_username(self): Custom username validation to check if the username is
            already in use.

    Description:
        This form class allows developers to create custom user registration forms
        with specific field attributes and validation rules. It extends Django's
        UserCreationForm to provide a tailored registration experience.

    Usage:
        To use this form in a Django view, create an instance of the form and pass it
        to the view's context. For example:

        ```python
        from .forms import CustomUserCreationForm

        def register_user(request):
            if request.method == 'POST':
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    # Process the form data and create a new user
                    # ...
            else:
                form = CustomUserCreationForm()

            return render(request, 'registration/register.html', {'form': form})
        ```
    """

    username = get_type_field(CharField, 150, True, 'Username', TextInput, [])
    password = get_type_field(
        CharField,
        150,
        True,
        'Password',
        PasswordInput,
        password_validators)
    first_name = get_type_field(CharField, 30, True, 'First Name', TextInput, [])
    last_name = get_type_field(CharField, 30, True, 'Last Name', TextInput, [])
    email = get_type_field(EmailField, 254, True, 'Email', TextInput, [])

    class Meta:
        """
        Meta:
            model (User): The User model associated with this form.
            fields (tuple): The fields to include in the form, including 'username',
                'password', 'first_name', 'last_name', and 'email'.
        """
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = (
            "Your password can’t be too similar to your other personal information. "
            "Your password must contain at least 8 characters. "
            "Your password can’t be a commonly used password. "
            "Your password can’t be entirely numeric.")

    def clean_username(self):
        """
        Validate and clean a username.

        This method is used as part of form validation to ensure that the provided
        username is unique and does not already exist in the User database.

        Returns:
            str: The cleaned and validated username if it is unique.

        Raises:
            ValidationError: If the provided username is not unique, a
            ValidationError is raised with a message indicating that the username
            is already in use.

        """
        username = self.cleaned_data['username']
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                'This username is already in use. Please choose another.')

        return username
