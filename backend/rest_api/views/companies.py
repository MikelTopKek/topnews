from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from company.models import Company
from company.serializers import CompanySerializer


class CompaniesViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'post', 'delete']

    @action(detail=False, methods=['get'])
    def list(self, request, *args, **kwargs):
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        post = Company.objects.get(id=self.kwargs['company_id'])
        serializer = CompanySerializer(post, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        user = Company.objects.get(id=self.kwargs['company_id'])
        user.delete()
        return Response(status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
