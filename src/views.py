"""
Module: views.py

This module defines views, viewsets, and related functions for the Django application,
including user authentication, posts, and profiles.

Views and ViewSets:
    - index: Default landing page view.
    - PostViewSet: ViewSet for handling Post model data.
    - UserViewSet: ViewSet for handling User model data with authentication.
    - CustomLoginView: Custom login view.
    - CustomLogoutView: Custom logout view.
    - signup: User registration view.
    - profile: User profile view.

"""

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from .models import Post
from .forms import CustomUserCreationForm
from .serializers import PostSerializer, CustomUserSerializer


def index(request):
    """
    index View

    Default landing page view.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the 'src/index.html' template.

    """
    return render(request, "src/index.html")


# ViewSets define the view behavior.


# pylint: disable=R0901
class PostViewSet(ModelViewSet):
    """
    PostViewSet Class

    ViewSet for handling Post model data.

    Attributes:
        queryset (QuerySet): The queryset for retrieving Post model instances.
        serializer_class (PostSerializer): The serializer class for Post model data.

    """

    # pylint: disable=E1101
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# pylint: disable=R0901
class UserViewSet(ModelViewSet):
    """
    UserViewSet Class

    ViewSet for handling User model data with authentication.

    Attributes:
        queryset (QuerySet): The queryset for retrieving User model instances.
        serializer_class (CustomUserSerializer): The serializer class for User model data.
        permission_classes (list): The list of permission classes, including IsAuthenticated.

    """

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


# pylint: disable=R0901
class CustomLoginView(LoginView):
    """
    CustomLoginView Class

    Custom login view.

    Attributes:
        template_name (str): The path to the login template.
        success_url (str): The URL to redirect to after successful login.

    """

    template_name = "src/login.html"
    success_url = "/profile/"


class CustomLogoutView(BaseLogoutView):
    """
    CustomLogoutView Class

    Custom logout view.

    Attributes:
        template_name (str): The path to the logout template.
        next_page (str): The URL to redirect to after logout (login page).

    """

    template_name = "src/logout.html"
    next_page = reverse_lazy("login")


def signup(request):
    """
    signup View

    User registration view.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the 'src/signup.html' template with the registration form.

    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the form, which includes first_name, last_name, and email fields
            form.save()

            # Log in the user after registration
            login(request, form.instance)

            # Redirect to the user's profile page
            return redirect("profile")
    else:
        form = CustomUserCreationForm()

    return render(request, "src/signup.html", {"form": form})


@login_required
def profile(request):
    """
    profile View

    User profile view.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the 'src/profile.html' template with user information.

    """
    # Fetch and display user information
    user = request.user
    return render(request, "src/profile.html", {"user": user})
