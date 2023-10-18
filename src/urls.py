"""
Module: urls.py

This module defines the URL patterns for the Django application,
including routes for users, posts, authentication, and other views.

URL Patterns:
    - Index: Default landing page.
    - Users: API routes for user-related views (using a DefaultRouter).
    - Posts: API routes for post-related views (using a DefaultRouter).
    - Signup: User registration view.
    - Profile: User profile view.
    - Login: Custom login view.
    - Logout: Custom logout view.

"""

from django.urls import path, include
from rest_framework import routers
from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"posts", views.PostViewSet)

auth_redirect = include("rest_framework.urls", namespace="rest_framework")

urlpatterns = [
    path("", views.index, name="index"),  # Default landing page.
    path("", include(router.urls)),  # API routes for users and posts.
    path("signup/", views.signup, name="signup"),  # User registration view.
    path("profile/", views.profile, name="profile"),  # User profile view.
    path("login/", views.CustomLoginView.as_view(), name="login"),  # Custom login view.
    path(
        "logout/", views.CustomLogoutView.as_view(), name="logout"
    ),  # Custom logout view.
]
