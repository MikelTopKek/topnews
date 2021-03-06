# pylint: disable= R0201, R0901
import logging.config

from django.conf import settings
from django.contrib.auth import get_user_model
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api.constants import ERROR_RESPONSE_EXAMPLE
from rest_api.permissions import IsSuperUser
from user.serializers import SignUpUserSerializer, SignUpAdminSerializer

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('main_logger')
UserModel = get_user_model()


class SignUpView(APIView):
    permission_classes = (IsAdminUser, )

    @swagger_auto_schema(
        operation_description='Register user',
        request_body=SignUpUserSerializer,
        responses={
            status.HTTP_201_CREATED: SignUpUserSerializer,
            status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE_EXAMPLE,
        }
    )
    def post(self, request):
        serializer = SignUpUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        username = serializer.data['username']
        logger.info(f'User {username} created')

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SignUpAdminView(APIView):
    permission_classes = (IsSuperUser, )

    @swagger_auto_schema(
        operation_description='Register admin user',
        request_body=SignUpAdminSerializer,
        responses={
            status.HTTP_201_CREATED: SignUpAdminSerializer,
            status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE_EXAMPLE,
        }
    )
    def post(self, request):
        serializer = SignUpAdminSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        username = serializer.data['username']
        logger.info(f'User {username} created')

        return Response(serializer.data, status=status.HTTP_201_CREATED)
