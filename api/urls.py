from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .viewsets import DocumentViewSet

router = DefaultRouter()

router.register(r'files', DocumentViewSet)

urlpatterns = [
    url('', include(router.urls))
]