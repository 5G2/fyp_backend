from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'first_name','last_name','password')

#to customise what data to be included in JWT token
class TokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        refresh["email"] = self.user.email
        refresh["first_name"] = self.user.first_name
        refresh["last_name"] = self.user.last_name

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data

class CutomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer