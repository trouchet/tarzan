"""
Module: serializers.py

This module defines serializers for the Django application, including serializers for
User and Post models.

Classes:
    - CustomUserSerializer: Serializes User model data for API representation.
    - PostSerializer: Serializes Post model data for API representation.

"""
# pylint: disable=R0903

from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from django.contrib.auth.models import User
from .models import Post

class CustomUserSerializer(HyperlinkedModelSerializer):
    """
    CustomUserSerializer Class

    Serializes User model data for API representation.
    """

    class Meta:
        """
        Meta:
            model (User): The User model to be serialized.
            fields (list): A list of fields to include in the serialized representation.

        Fields:
            - url (HyperlinkedIdentityField): The URL to the user's detail view.
            - username (CharField): The username of the user.
            - email (EmailField): The email address of the user.
            - is_staff (BooleanField): Indicates whether the user is a staff member.
        """
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostSerializer(ModelSerializer):
    """
    PostSerializer Class

    Serializes Post model data for API representation.
    """

    class Meta:
        """
        Meta:
        model (Post): The Post model to be serialized.
        fields (str or list): Specifies which fields to include in the serialized representation.
            - '__all__': Includes all fields from the Post model.
        """

        model = Post
        fields = '__all__'
