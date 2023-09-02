from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth.views  import PasswordResetView, \
    PasswordResetDoneView, \
    PasswordResetConfirmView, \
    PasswordResetCompleteView

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

auth_redirect=include('rest_framework.urls', namespace='rest_framework')

urlpatterns = [
    path('', views.index, name="index"),
    path('', include(router.urls)),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]


