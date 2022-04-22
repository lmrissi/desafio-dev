from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import FileUploadView, ListTransactionsView

urlpatterns = [
    path("upload/", FileUploadView.as_view(), name="file_upload_view"),
    path("list/", ListTransactionsView.as_view(), name="list_transactions_view")
]