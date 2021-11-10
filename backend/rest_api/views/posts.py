from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostSerializer


class PostsView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)
