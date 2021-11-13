import logging.config

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostPostSerializer, PostSerializer

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('main_logger')


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    post_serializer_class = PostPostSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

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
        serializer = PostPostSerializer(post, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'Post {post} updated')
        return Response(serializer.data)
