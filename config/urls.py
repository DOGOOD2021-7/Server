
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('gyms/', include('gym.urls')),
    path('reservations/', include('reservation.urls')),
    path('clients/', include('client.urls')),
]
