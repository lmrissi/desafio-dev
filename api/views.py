from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status

from .models import Cnab
from .utils import parse_cnab_file

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        
        parsed_cnab_dict_list = parse_cnab_file(request.data['file'])

        Cnab.objects.save_parsed_cnab(parsed_cnab_dict_list)

        return Response(status=status.HTTP_201_CREATED)