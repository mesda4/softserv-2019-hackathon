#from django.shortcuts import render
from django.contrib.auth import login, authenticate, user_logged_in
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
#from data.backends import *
from django.contrib.auth import  login
#from rest_framework_jwt.settings import api_settings
#from rest_framework import parsers
#from data.models import *
#from .serializers import *
#import datetime
from braces.views import CsrfExemptMixin
from django.conf import settings
from rest_framework_jwt.settings import api_settings
import jwt
#from django.core.mail import send_mail
#from django.template.loader import render_to_string

from .serializers import *
from animals.models import *

#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER


class AnimalsView(CsrfExemptMixin, generics.GenericAPIView):
    serializer_class = AnimalsSerializer
    queryset=Animal.objects.all()
    permission_classes = ( permissions.AllowAny, )

    def get(self, request):
        serializer = self.get_serializer(Animal.objects.all(), many=True)
        return Response(serializer.data, status=200)


class AnimalView(CsrfExemptMixin, generics.GenericAPIView):
    serializer_class = AnimalSerializer
    permission_classes = ( permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'status': 'Error', 'message': str(serializer.errors)}, status=400)


class AnimalsView(CsrfExemptMixin, generics.GenericAPIView):
    serializer_class = AnimalsSerializer
    #queryset=Animal.objects.all()
    permission_classes = ( permissions.AllowAny, )

    def get(self, request):
        serializer = self.get_serializer(Animal.objects.all(), many=True)
        return Response(serializer.data, status=200)

