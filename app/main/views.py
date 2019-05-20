from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from main.models import User
from main.serializers import UserProfileSerializer, CreateUserSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class CreateUserViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer
