from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    genre = models.CharField(max_length=50)
    year = models.IntegerField()

    


    def __str__(self):
        return self.title
    

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name
    

class CommitBook(models.Model):
    title = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    create_ed =  models.DateField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)