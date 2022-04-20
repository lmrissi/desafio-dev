from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import re_path, path

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'))
]