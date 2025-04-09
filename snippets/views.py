from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book,Users
from .serializers import BookSerializer,UserSerializer
from django.shortcuts import get_object_or_404







@api_view(['GET','POST'])
def book_list(request):

    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books,many = True)
        return Response(serializer.data)
    

    elif request.method == "POST":
        serializer = BookSerializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET","PUT","PATCH","DELETE"])
def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)
    

    elif request.method == "PUT":
        serializer = BookSerializer(book,data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PATCH":
        serializer = BookSerializer(book,data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == "GET":
        # User.objects.all() - queryset qaytaradi, va many=True flagi kerak
        users = Users.objects.all()  
        serializer = UserSerializer(users, many=True)  # many=True, chunki bir nechta foydalanuvchi
        print(serializer.data,"99====================================================================")
        return Response(serializer.data)

    elif request.method == "POST":
        # Yangi foydalanuvchi qo‘shish
        serializer = UserSerializer(data=request.data)
        print(serializer.data,"0====================================================================")
        
        
        if serializer.is_valid():
            # Serializerni print qilish va tekshirish
            print(serializer.data,"1====================================================================")
 
            serializer.save()
            print(serializer.data,"2====================================================================")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    

        
        
     
     
     
