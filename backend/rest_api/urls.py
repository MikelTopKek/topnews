from django.urls import path

from rest_api.views import UsersView, CompaniesView, PostsView

urlpatterns = [
    path('user/', UsersView.as_view({'get': 'list'}), name='users_details'),
    path('post/', PostsView.as_view({'get': 'list'}), name='posts_details'),
    path('company/', CompaniesView.as_view({'get': 'list'}), name='companies_details'),
]
