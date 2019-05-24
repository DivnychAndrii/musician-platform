from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from main.models import User
from main.serializers import UserProfileSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowAny,)

    def get_object(self):
        return self.request.user

    @shared_task
    def send_mail(self, user_id):
        user = get_user_model().objects.filter(id=user_id)
        user = user.first()
        title = 'Verify'
        mail_message = f'Follow this link to verify your account'
        mail = EmailMultiAlternatives(title, mail_message, to=[user.email])
        mail.attach_alternative(mail_message, mimetype=mail_message)
        mail.send()
