from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import re_path, path

from .views import FileUploadView
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view(), name='file_upload_view')
]