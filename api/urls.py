from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import FileUploadView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload_view')
]