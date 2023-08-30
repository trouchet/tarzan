from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer, UserSerializer

def index(request):
    return render(request, 'src/index.html')

# ListAPIView define the view behavior.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# ViewSets define the view behavior.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

