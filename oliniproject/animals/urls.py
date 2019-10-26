from django.urls import include, path
from .views import *

urlpatterns = [
    path('list/', Animals.as_view()),
]

