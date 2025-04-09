from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     path('book/',book_list),
     path('book_detail/<int:pk>/',book_detail,name='book_detail'),
     path('user/',user_list)

]