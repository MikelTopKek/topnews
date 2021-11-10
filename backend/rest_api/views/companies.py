from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from company.models import Company
from company.serializers import CompanySerializer


class CompaniesView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)
