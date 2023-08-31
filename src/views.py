from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Post

from .serializers import PostSerializer, UserSerializer

def index(request):
    return render(request, 'src/index.html')

# ViewSets define the view behavior.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]