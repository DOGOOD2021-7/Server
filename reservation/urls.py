from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('', ReservationList.as_view()),
    path('<int:pk>', ReservationsDetail.as_view()),
    path('gyms/<int:pk>', AddReservation.as_view())

]