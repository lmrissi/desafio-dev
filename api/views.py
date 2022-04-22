from audioop import avg
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status

from .models import Cnab, Store
from .utils import parse_cnab_file, save_parsed_cnab, is_store_saved, list_cnabs_by_store

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        if "file" not in request.data:
            raise ParseError("Empty content")

        save_parsed_cnab(parse_cnab_file(request.data["file"]))

        return Response(status=status.HTTP_201_CREATED)

class ListTransactionsView(APIView):
    def get(self, request):
        stores = Store.objects.all()

        cnabs = Cnab.objects.all().order_by("date")

        result = list_cnabs_by_store(stores, cnabs)
        
        return Response(result, status=status.HTTP_200_OK)