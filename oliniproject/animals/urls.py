from django.urls import include, path
from .views import *

urlpatterns = [
    path('list/', AnimalsView.as_view()),
    path('list1/', AnimalView.as_view()),
]

