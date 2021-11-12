from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostPostSerializer, PostSerializer


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    post_serializer_class = PostPostSerializer
    http_method_names = ['get', 'post', 'delete']

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
        user = Post.objects.get(id=self.kwargs['post_id'])
        user.delete()
        return Response(status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
