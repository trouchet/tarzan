from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from django.contrib.auth.models import User

from .models import Post

# Serializers define the API representation.


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
