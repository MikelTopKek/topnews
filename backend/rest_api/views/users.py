from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.serializers import UserGetSerializer

UserModel = get_user_model()


class UserViewSet(ModelViewSet):
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
