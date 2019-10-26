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
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

# Create your views here.

class RegistrationAPI(generics.GenericAPIView, CsrfExemptMixin):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response(status=405)

    def post(self, request, *args, **kwargs):
        userData = request.data.pop('user', None)
        #userData = {}
        #userData['email'] = request.data['email']
        #userData['password'] = request.data['password']
        if not userData:
            return Response({'status': 'error', 'message': 'User data is absent'}, status=400)
        print(userData)
        serializer = self.get_serializer(data=userData)
        print(type(serializer))
        if serializer.is_valid():
            user = serializer.save()
            response = {}
            response['user'] = serializer.data
            payload = jwt_payload_handler(user)
            token = token = jwt.encode(payload, settings.SECRET_KEY)
            response['token'] = token
            user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
            return Response(response, status=200)
        return Response(serializer.errors, status=422)

class LoginAPI(generics.GenericAPIView, CsrfExemptMixin):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        user = request.data.pop('user')
        try:
            email = user['email']
            password = user['password']

            user = User.objects.get(email=email, password=password)
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
                    user_details = {}
                    user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                    return Response(user_details, status=200)

                except Exception as e:
                 raise e
            else:
                res = {
                    'error': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=403)
        except KeyError:
            res = {'error': 'please provide a email and a password'}
            return Response(res)


class UserInfo(generics.GenericAPIView, CsrfExemptMixin):
    permission_classes = (permissions.IsAuthenticated ,)
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = self.get_serializer(user)
        #serializer.is_valid()
        print(serializer.data)
        #print()
        return(Response(serializer.data, status=200))



