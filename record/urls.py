
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',AddRecord.as_view()),
    path('<int:pk>', OneRecord.as_view()),
]