from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import re_path, path

from .viewsets import DocumentViewSet
from .views import FileUploadView
from django.views.generic import TemplateView

router = DefaultRouter()

router.register(
        r'files', DocumentViewSet,
    )

urlpatterns = [
    url('', include(router.urls)),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view(), name='file_upload_view')
]