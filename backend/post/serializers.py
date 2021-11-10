from rest_framework.serializers import ModelSerializer

from company.models import Company


class PostSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'title', 'user_id', 'text', 'topic')
