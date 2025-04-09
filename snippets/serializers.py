from rest_framework import serializers

from .models import Book,Users


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
          model = Users
          fields = '__all__'
