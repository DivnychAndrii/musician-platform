from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models

<<<<<<< HEAD

class UserProfileViewSet(viewsets.ModelViewSet):
=======
'''
def index(request):

    return render(request, "index.html",)

'''

>>>>>>> 95f7f198ccf9cd0e3ab59508009f3dddf5005089

    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()


def index(request):

    return render(request, 'index.html')


