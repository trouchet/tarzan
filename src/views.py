from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView

from .models import Post
from .forms import CustomUserCreationForm
from .serializers import PostSerializer, CustomUserSerializer

def index(request):
    return render(request, 'src/index.html')

# ViewSets define the view behavior.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class CustomLoginView(LoginView):
    template_name = 'src/login.html'

    # Replace with the desired URL
    success_url = '/profile/'

class CustomLogoutView(BaseLogoutView):
    # Use your custom template
    template_name = 'src/logout.html'

    # Redirect to the login page after logout
    next_page = reverse_lazy('login')       

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the form, which includes first_name, last_name, and email fields
            form.save()                     

            # Log in the user after registration
            login(request, form.instance)

            # Redirect to the user's profile page   
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'src/signup.html', {'form': form})

@login_required
def profile(request):
    # Fetch and displa  y user information
    user = request.user
    return render(request, 'src/profile.html', {'user': user})