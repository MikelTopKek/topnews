# pylint: disable=R0901, W0613, R0201
import logging.config

from django.conf import settings
from django.db import transaction
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import (PostManySerializer, PostPostSerializer,
                              PostSerializer)
from rest_api.constants import ERROR_RESPONSE_EXAMPLE, SUCCESS_RESPONSE_EXAMPLE
from rest_api.permissions import PermissionsPostsMixin
from user.choices import CLIENT

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('main_logger')


class PostsViewSet(PermissionsPostsMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    post_serializer_class = PostPostSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put']

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            if hasattr(self, 'post_serializer_class'):
                return self.post_serializer_class
        return super().get_serializer_class()

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['post_id'])
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['post_id'])

        if self.request.user.id != post.user.id:
            return Response('You don`t have permission to delete this post')

        post.delete()
        logger.info(f'Post {post} deleted')
        return Response(status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        title = serializer.data['title']
        user = self.request.user
        logger.info(f'Post {title} from user {user} created')

    def partial_update(self, request, *args, **kwargs):
        post = Post.objects.get(id=self.kwargs['post_id'])

        if self.request.user.id != post.user.id and self.request.user.user_type == CLIENT:
            return Response('You don`t have permission to change this post')

        serializer = PostPostSerializer(post, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'Post {post} updated')
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description='Bulk update posts topic',
        request_body=openapi.Schema(
            description="Data to update posts",
            type=openapi.TYPE_OBJECT,
            properties={
                "old_topic": openapi.Schema(type=openapi.TYPE_STRING),
                "new_topic": openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            status.HTTP_200_OK: SUCCESS_RESPONSE_EXAMPLE,
            status.HTTP_400_BAD_REQUEST: ERROR_RESPONSE_EXAMPLE,
        }
    )
    @transaction.atomic
    @action(detail=False, methods=['put'])
    def bulk_update(self, request, *args, **kwargs):

        serializer = PostManySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        posts = Post.objects.filter(topic=data['old_topic'])

        for post in posts:
            post.topic = data['new_topic']
        Post.objects.bulk_update(posts, ['topic'])
        return Response({"message": 'ok'})
