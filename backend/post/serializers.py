from rest_framework import serializers
from rest_framework.fields import HiddenField

from post.models import Post
from user.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'topic', 'user')


class PostPostSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'topic', 'user')
