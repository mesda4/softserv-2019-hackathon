# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
from django.urls import path
from needs.views import *

urlpatterns = [
    path('need', NeedAPI.as_view()),
    path('need/<int:pk>', NeedDetailAPI.as_view()),
    path('need-type', NeedTypeAPI.as_view()),
    path('need-type/<int:pk>', NeedTypeDetailAPI.as_view()),
    # path('need', AnimalNeedAPI.as_view()),
    # path('need/<int:pk>', AnimalNeedDetailAPI.as_view()),
]