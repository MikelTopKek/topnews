from rest_framework import serializers

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


class PostManySerializer(serializers.Serializer):

    old_topic = serializers.CharField(max_length=64)
    new_topic = serializers.CharField(max_length=64)
