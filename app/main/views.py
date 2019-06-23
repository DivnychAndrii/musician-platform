from PIL import Image
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from rest_framework import viewsets, mixins, status, views
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from app import settings
from main.models import User
from main.permissions import IsGetOrAuthenticated
from main.serializers import UserProfileSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         viewsets.GenericViewSet):

    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsGetOrAuthenticated,)

    def get_object(self):
        return self.request.user

    # @shared_task
    # def send_mail(self, user_id):
    #     user = get_user_model().objects.filter(id=user_id)
    #     user = user.first()
    #     title = 'Verify'
    #     mail_message = f'Follow this link to verify your account'
    #     mail = EmailMultiAlternatives(title, mail_message, to=[user.email])
    #     mail.attach_alternative(mail_message, mimetype=mail_message)
    #     mail.send()


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        try:
            file = request.data['file']
        except KeyError:
            raise KeyError('Request has no avatar attached')

        user = request.user
        user.avatar.save(file.name, file, save=True)
        image = Image.open(user.avatar)
        image.thumbnail((128, 128))
        image.save(settings.MEDIA_ROOT + 'images/' + file.name)
        user.avatar = image

        return Response(status.HTTP_202_ACCEPTED)
