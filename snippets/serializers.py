from rest_framework import serializers

from .models import Book,CommitBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','pages','genre','year']


class CommitSerializer(serializers.ModelSerializer):
     class Meta:
         model = CommitBook
         fields = "__all__"