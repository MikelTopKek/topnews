from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from rest_api.views import (CompaniesViewSet, PostsViewSet, SignUpView,
                            UserViewSet)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='users_details'),
    path('users/<int:user_id>/', UserViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='user_details'),
    path('posts/', PostsViewSet.as_view({'post': 'create', 'get': 'list'}), name='posts_details'),
    path('posts/<post_id>/',
         PostsViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update','delete': 'destroy'}), name='posts_details'),
    path('companies/', CompaniesViewSet.as_view({'post': 'create', 'get': 'list'}), name='companies_details'),
    path('companies/<company_id>/',
         CompaniesViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='company_details'),
]
