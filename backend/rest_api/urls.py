from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from rest_api.views import UsersView, CompaniesView, PostsView, SignUpView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user_details'),
    path('user/', UsersView.as_view({'get': 'list'}), name='users_details'),
    path('post/', PostsView.as_view({'get': 'list'}), name='posts_details'),
    path('company/', CompaniesView.as_view({'get': 'list'}), name='companies_details'),
]
