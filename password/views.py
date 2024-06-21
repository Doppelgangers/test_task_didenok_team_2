from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from password.models import PasswordStorage
from password.serializers import PasswordSerializer, PasswordReadSerializer, SearchPasswordSerializer


class PasswordView(APIView):

    def get(self, request: Request, service_name: str) -> Response:
        password: PasswordStorage = get_object_or_404(PasswordStorage, service_name=service_name)
        return Response(PasswordReadSerializer(password).data)

    def post(self, request: Request, service_name: str) -> Response:
        data = request.POST.copy()
        data['service_name'] = service_name
        serializer = PasswordSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        response = Response(serializer.data)
        serializer.save()
        return response


class SearchPasswordView(APIView):

    def get(self, request: Request) -> Response:
        serializer = SearchPasswordSerializer(data=request.query_params)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        list_password: list[PasswordStorage] = PasswordStorage.objects.filter(
            service_name__icontains=serializer.validated_data['service_name'])
        return Response(PasswordReadSerializer(list_password, many=True).data)
