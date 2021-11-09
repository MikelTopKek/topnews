from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from company.serializers import CompanySerializer
from post.models import Post


class PostsView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CompanySerializer

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)
