# pylint: disable=R0901
import logging.config

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_api.permissions import PermissionsUsersMixin
from user.serializers import UserGetSerializer

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('main_logger')

UserModel = get_user_model()


class UserViewSet(PermissionsUsersMixin, ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserGetSerializer
    http_method_names = ['get', 'delete']

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=self.kwargs['user_id'])
        serializer = UserGetSerializer(user, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=self.kwargs['user_id'])
        user.delete()
        logger.info(f'User {user} deleted')
        return Response(status.HTTP_200_OK)
