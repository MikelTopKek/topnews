from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer


UserModel = get_user_model()


class UserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'created_at', 'updated_at', 'telephone_number', 'user_type', 'avatar')


class SignUpUserSerializer(UserSerializer):
    password = CharField(required=True, write_only=True)

    def create(self, request):
        user = UserModel.objects.create(
            username=request['username'],
            first_name=request['first_name'],
        )

        user.set_password(request['password'])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'first_name', 'last_name', 'password')

