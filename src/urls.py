from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

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
    path('api-auth/', auth_redirect),
]
