from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', GymList.as_view()),
    path('<int:pk>', GymDetail.as_view()),
    path('<int:pk>/reservations', ReservationTimeDetail.as_view())

]