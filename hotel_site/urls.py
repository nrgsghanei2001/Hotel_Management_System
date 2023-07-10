from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
]