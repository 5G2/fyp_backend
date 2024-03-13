from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'username','password')

#to customise what data to be included in JWT token
class TokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        refresh["email"] = self.user.email
        refresh["username"] = self.user.username

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["role"]=self.user.role
        data["username"]=self.user.username
        return data

class CutomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer