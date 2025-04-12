from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    pages = models.IntegerField()
    genre = models.CharField(max_length=50)
    year = models.IntegerField()

    


    def __str__(self):
        return self.title
    

class CommitBook(models.Model):
    title = models.CharField(max_length=250)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    create_ed =  models.DateField(auto_now_add=True)
    update_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.book.title}"