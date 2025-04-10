from django.contrib import admin
from django.urls import path,include
from .views import *




urlpatterns = [
path('book_get/',BookView.as_view()),
path('book_detail/<int:pk>/',BookDetailView.as_view())
]