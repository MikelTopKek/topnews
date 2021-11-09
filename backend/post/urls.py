from django.urls import path

from company.views import CompaniesView

urlpatterns = [
    path('post/', CompaniesView.as_view({'get': 'list'}), name='posts_details'),
]
