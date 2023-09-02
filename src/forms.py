# forms.py
from django.contrib.auth.forms import UserCreationForm

from django.forms import CharField, \
    EmailField, \
    PasswordInput, \
    ValidationError, \
    TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

from . import utils


def labelInput(text, is_required):
    if is_required:
        label_text = f'{text}*'
    else:
        label_text = text
    return label_text


def getTypeField(
        type_field,
        max_length_value,
        is_required,
        label,
        input_type,
        validators_list):
    return type_field(
        max_length=max_length_value,
        required=is_required,
        widget=input_type(
            attrs={
                'placeholder': labelInput(
                    label,
                    is_required),
                'class': 'form-control'}),
        validators=validators_list,
    )


password_validators = [
    password_validation.validate_password,  # Password similarity check
    utils.validate_password_length,         # Password length check
    utils.validate_common_password,         # Commonly used password check
    utils.validate_password_numeric,        # Numeric check
]


class CustomUserCreationForm(UserCreationForm):
    username = getTypeField(CharField, 150, True, 'Username', TextInput, [])
    password = getTypeField(
        CharField,
        150,
        True,
        'Password',
        PasswordInput,
        password_validators)
    first_name = getTypeField(CharField, 30, True, 'First Name', TextInput, [])
    last_name = getTypeField(CharField, 30, True, 'Last Name', TextInput, [])
    email = getTypeField(EmailField, 254, True, 'Email', TextInput, [])

    class Meta:
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
        username = self.cleaned_data['username']
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                'This username is already in use. Please choose another.')

        return username
