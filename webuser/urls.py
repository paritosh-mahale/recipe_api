from django.urls import path
from .views import UserView
from rest_framework.authtoken import views

urlpatterns = [
    path('', UserView.as_view(), name="create_user"),
    path('login/', views.obtain_auth_token, name="login_user"),
]