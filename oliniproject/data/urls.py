from django.urls import include, path
from .views import *

urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('info/', UserInfo.as_view()),
]

