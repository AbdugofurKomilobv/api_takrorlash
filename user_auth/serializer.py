from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['name']=user.username
        token['salom']='hi'
        token["is_admin"]=user.is_superuser

        return token
    
    


User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")


        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"User does not exist"
                }
            )
        auth_user = authenticate(username=user.username,password=password)
        if auth_user is None:
            raise serializers.ValidationError(
                {
                    "success": False,
                    "detail": "Username or password is invalid"
                }
            )
        attrs["user"]=auth_user
        return  attrs