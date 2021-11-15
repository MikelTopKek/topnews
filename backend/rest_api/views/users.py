# pylint: disable=R0901
import logging.config

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_api.permissions import PermissionsUsersMixin
from user.choices import CLIENT
from user.serializers import UserGetSerializer, UserUpdateSerializer

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('main_logger')

UserModel = get_user_model()


class UserViewSet(PermissionsUsersMixin, ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserGetSerializer
    update_serializer_class = UserUpdateSerializer
    http_method_names = ['get', 'delete', 'patch']

    def get_serializer_class(self):
        if self.action in ['partial_update']:
            if hasattr(self, 'update_serializer_class'):
                return self.update_serializer_class
        else:
            return self.serializer_class
        return super().get_serializer_class()

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

    def partial_update(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=self.kwargs['user_id'])
        logger.info(f'{self.request.__dir__()}')
        logger.info(f'{self.request.user.id}')
        if self.request.user.id != user.id and self.request.user.user_type == CLIENT:
            return Response('You don`t have permission to change this post')

        serializer = UserUpdateSerializer(user, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'User {user} updated')
        return Response(serializer.data)


class UserDetailView(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserGetSerializer
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=self.request.user.id)
        serializer = UserGetSerializer(user, context={'request': request})
        return Response(serializer.data)
