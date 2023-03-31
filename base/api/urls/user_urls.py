from django.urls import path
from base.api.views import user_views as views
from base.api.views.user_views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('users/profile/', views.getUsersProfile, name="users-profile"),
    path('users/profile/update/', views.updateUsersProfile,
         name="users-profile-update"),
    path('users/', views.getUsers, name="users"),
    path('users/register/', views.registerUser, name="users-register"),
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name="token-obtain-pair"),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/<str:pk>/', views.getUserById, name='user'),

    path('users/update/<str:pk>/', views.updateUser, name='user-update'),
    path('users/delete/<str:pk>/', views.deleteUser, name='user-delete'),

]
