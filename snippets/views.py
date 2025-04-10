from django.shortcuts import render
from rest_framework import generics,status,viewsets
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .models import Book,Users
from .serializers import BookSerializer,UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView




class BookView(APIView):
    
    def get(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book,many = True)
        return Response({
            "success":True,
            "count":book.count(),
            "data":serializer.data
        })
    def post(self,request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(
                    {
                        "success":True,
                        "message": "Book created successfully",
                        "data":serializer.data
                    },status.HTTP_201_CREATED
                )
            except Exception as a:
                return Response(
                    {
                        "success": False,
                        "error": str(a)
                    },status.HTTP_500_INTERNAL_SERVER_ERROR
                )

           
                   
class BookDetailView(APIView):
        def get(self,request,pk):
            book = get_object_or_404(Book,pk=pk)
            serializer = BookSerializer(book)
            return Response({
                "success": True,
                "data": serializer.data
            },status.HTTP_200_OK)
       
                
        def put(self,request,pk):
         book = get_object_or_404(Book,pk=pk)
         serializer = BookSerializer(book,data = request.data)
         if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                return Response(
                         {
                    "success": True,
                    "messege": "Muvofaqyatli taxrirlandi",
                    "data": serializer.data
                },status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {
                        "success": False,
                        "errors":str(e)
                    },status.HTTP_500_INTERNAL_SERVER_ERROR
                )
