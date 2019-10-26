import datetime
from pprint import pprint
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from needs.models import *
from needs.serializers import NeedTypeSerializer, NeedSerializer
from rest_framework import generics
from django.http import JsonResponse

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

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from django.core.mail import send_mail
#from django.template.loader import render_to_string

from .serializers import *


class NeedAPI(generics.GenericAPIView, CsrfExemptMixin):
    queryset = OrpanageNeed.objects.all()
    serializer_class = NeedSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        need = OrpanageNeed.objects.all()
        serializer = self.serializer_class(need, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        serializer = self.serializer_class(data=request.data)
        pprint(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NeedDetailAPI(generics.GenericAPIView, CsrfExemptMixin):
    serializer_class = NeedSerializer
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return OrpanageNeed.objects.get(pk=pk)
        except OrpanageNeed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        need = self.get_object(pk)
        serializer = self.serializer_class(need)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        need = self.get_object(pk)
        serializer = self.serializer_class(need, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        need = self.get_object(pk)
        need.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NeedTypeAPI(generics.GenericAPIView, CsrfExemptMixin):
    queryset = NeedType.objects.all()
    serializer_class = NeedTypeSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        need = NeedType.objects.all()
        serializer = self.serializer_class(need, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NeedTypeDetailAPI(generics.GenericAPIView, CsrfExemptMixin):
    queryset = NeedType.objects.all()
    serializer_class = NeedTypeSerializer
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return NeedType.objects.get(pk=pk)
        except NeedType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        need = self.get_object(pk)
        serializer = self.serializer_class(need)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        need = self.get_object(pk)
        serializer = self.serializer_class(need, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        need = self.get_object(pk)
        need.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
