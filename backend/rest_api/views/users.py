from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserGetSerializer
from rest_framework.viewsets import ModelViewSet

UserModel = get_user_model()


class UserDetailView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        user = UserModel.objects.get(id=user_id)
        serializer = UserGetSerializer(user, context={'request': request})
        return Response(serializer.data)


class UsersView(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserGetSerializer

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)

