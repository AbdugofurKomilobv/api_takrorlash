from rest_framework import serializers

from .models import Book,Users


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    model = Users
    fields = ['id', 'first_name', 'last_name', 'email']