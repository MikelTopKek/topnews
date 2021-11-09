from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import UserSerializer

UserModel = get_user_model()


class UserDetailView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        user = UserModel.objects.get(id=user_id)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)


class UsersView(APIView):

    def get(self, request):
        users = UserModel.objects.all()
        return Response(users)
