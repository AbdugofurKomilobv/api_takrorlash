# django imporlar
from django.shortcuts import render


# rest imporlar
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# maxalliy importlar
from .make_token import *

from .serializer import *


class LoginApi(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
         
        
        user = serializer.validated_data.get("user")
        token = get_tokens_for_user(user)
        token["salom"]= "hi"
        token["is_admin"]= user.is_superuser

        return Response(data=token,status=status.HTTP_200_OK)
