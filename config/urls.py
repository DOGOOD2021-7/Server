
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('gyms/', include('gym.urls')),
    path('reservations/', include('reservation.urls')),
    path('records/',include('record.urls')),
    path('clients/', include('client.urls')),
    path('coaching/',include('coaching.urls')),
]
