# forms.py
from django.contrib.auth.forms import UserCreationForm

from django.forms import CharField, EmailField, PasswordInput, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from . import utils

class CustomUserCreationForm(UserCreationForm):
    password = CharField(
        max_length=150,
        widget=PasswordInput,
        validators=[
            password_validation.validate_password,  # Password similarity check
            utils.validate_password_length,         # Password length check
            utils.validate_common_password,         # Commonly used password check
            utils.validate_password_numeric,        # Numeric check
        ]
    )
    first_name = CharField(
        max_length=30, 
        required=True, 
        help_text='Required. Enter your first name.')
    last_name = CharField(
        max_length=30, 
        required=True, 
        help_text='Required. Enter your last name.'
    )
    email = EmailField(
        max_length=254, 
        required=True, 
        help_text='Required. Enter a valid email address.'
    )


    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text =  (
            "Your password can’t be too similar to your other personal information. "
            "Your password must contain at least 8 characters. "
            "Your password can’t be a commonly used password. "
            "Your password can’t be entirely numeric."
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already in use. Please choose another.')

        return username