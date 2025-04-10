from rest_framework import serializers

from .models import Book,Users,CommitBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
          model = Users
          fields = '__all__'

class CommitSerializer(serializers.ModelSerializer):
     class Meta:
         model = CommitBook
         fields = '__all__'