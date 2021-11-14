# pylint: disable=W0221
from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from company.serializers import CompanySerializer

UserModel = get_user_model()


class SignUpUserSerializer(ModelSerializer):
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


class UserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name')


class UserGetSerializer(ModelSerializer):

    company = CompanySerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'created_at', 'updated_at', 'telephone_number', 'user_type', 'avatar', 'company')
