from django.shortcuts import render
from rest_framework import generics,status,viewsets
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .models import Book,CommitBook
from .serializers import BookSerializer,CommitSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



# Ktob qoshish uchun api
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

           
#Comentarya uchun api  
class BookDetailView(APIView):
        permission_classes = [IsAuthenticated]
        # authentication_classes = [TokenAuthentication]
        
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
        def patch(self,request,pk):
            book = get_object_or_404(Book,pk=pk)
            serializer = BookSerializer(book,data = request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                try:
                    serializer.save()
                    return Response({
                        "success":True,
                        "message":"Muvofaqyatli O'zgartirildi",
                        "data": serializer.data
                    },status.HTTP_200_OK)
                except Exception as e:
                    return Response({
                        "success": False,
                        "errors": str(e)
                    },status.HTTP_500_INTERNAL_SERVER_ERROR)
        def delete(self,request,pk): 
            try: 
                book = get_object_or_404(Book,pk=pk)
                book.delete()
                return Response({
                        "success":True,
                        "message": "O'chirildi"
                    },status.HTTP_204_NO_CONTENT)
            except Exception as a:
                    return Response({
                        "succes":False,
                        "errors":str(a)
                    },status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommitBookApiView(APIView):


     
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


   
    def get(self,request):
        # faqat o'zimni comntlarimni olaman
        try:
            commits = CommitBook.objects.all()
            serializer = CommitSerializer(commits,many =True)
            return Response(serializer.data, status.HTTP_200_OK)
        except CommitBook.DoesNotExist:
            return Response({
                "detail": " comentaryalar topilmadi"
            },status.HTTP_404_NOT_FOUND)
  
    def post(self,request,book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"detail":"bunday kitob topilmadi"},status.HTTP_404_NOT_FOUND)
        serializer = CommitSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(book=book,author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
      

class CommitDetailBook(APIView):
     permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
     def get(self,request,book_id):
         try:
            commits = CommitBook.objects.filter(book_id=book_id, author = request.user)
            serializer = CommitSerializer(commits,many =True)
            return Response(serializer.data,status.HTTP_200_OK)
         except CommitBook.DoesNotExist:
             return Response({
                 "detail": "Xali comment yozmagansiz"
                 },status.HTTP_404_NOT_FOUND)
         


     def put(self,request,book_id,pk):
         try:
             commit = CommitBook.objects.get(pk=pk,book_id=book_id, author=request.user)
         except CommitBook.DoesNotExist:
             return Response({"errors":"buday coment mavjud emas"})
        
         
         
    


