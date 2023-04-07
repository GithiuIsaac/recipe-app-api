"""
URL Mappings for the User API.
"""
from django.urls import path

from user import views

# Used for the reverse mapping defined in test_user_api
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token')
]