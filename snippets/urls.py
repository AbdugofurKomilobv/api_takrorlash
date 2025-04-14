from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
#for book api 
path('book_get/',BookView.as_view()),
path('book_detail/<int:pk>/',BookDetailView.as_view()),
# ========================================================
# for commit api
path('commit/',CommitBookApiView.as_view()),
path("commit_detail/<int:book_id>/",CommitDetailBook.as_view()),
path("commit_detail/<int:book_id>/<int:pk>/",CommitDetailBook.as_view()),

]