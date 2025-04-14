from django.urls import path
from .views import LoginApi

urlpatterns = [
    path('login_api/',LoginApi.as_view())
]