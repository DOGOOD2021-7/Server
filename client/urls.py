from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ClientList.as_view()),
    path('<int:pk>/records/', ClientDetail.as_view()),

]