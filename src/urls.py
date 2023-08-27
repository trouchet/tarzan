from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.png")),
    ),
    url(r'^$', get_swagger_view(title='Pastebin API'))
]
