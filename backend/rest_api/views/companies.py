import logging.config

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from company.models import Company
from company.serializers import CompanySerializer

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('main_logger')


class CompaniesViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'post', 'delete', 'patch']

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        post = Company.objects.get(id=self.kwargs['company_id'])
        serializer = CompanySerializer(post, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        company = Company.objects.get(id=self.kwargs['company_id'])
        company.delete()
        logger.info(f'Company {company} deleted')
        return Response(status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
        name = serializer.data['name']
        logger.info(f'Company {name} created')

    def partial_update(self, request, *args, **kwargs):
        company = Company.objects.get(id=self.kwargs['company_id'])
        serializer = CompanySerializer(company, data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f'Company {company} updated')
        return Response(serializer.data)
