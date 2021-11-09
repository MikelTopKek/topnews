from rest_framework.serializers import ModelSerializer

from company.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'url', 'address', 'created_at')
