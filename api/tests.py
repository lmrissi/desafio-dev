import json
from django.test import Client
from rest_framework import status
from rest_framework.exceptions import ParseError
import unittest
from unittest.mock import MagicMock, patch
from rest_framework.response import Response

from api.views import ListTransactionsView
from .mocks import mocked_cnab_list_by_store

class TestFileUploadView(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/upload/"

    def test_should_return_status_201_when_upload_file_correctly(self):
        # Execution
        with open("documents/CNAB.txt", "r") as file:
            data = {"file": file}
            response = self.client.post(self.url, data)

         # Assertion
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_return_ParseError_and_status_400_when_upload_without_file(self):
        # Execution
        response = self.client.post(self.url)

        # Assertion
        self.assertRaises(ParseError)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestListTransactionsView(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/list/"
        self.expected_result = mocked_cnab_list_by_store

    @patch("api.views.ListTransactionsView.get")
    def test_should_return_status_200_and_mocked_content(self, list_transactions_view_get):
        # Mock
        list_transactions_view_get.return_value = Response(
                self.expected_result,
                status=status.HTTP_200_OK
            )
        
        # Execution
        response = self.client.get(self.url)

        # Assertion
        self.assertEqual(json.loads(response.content.decode('utf-8')), self.expected_result)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
