from django.urls import path
from . import views


urlpatterns = [
    path('visit_rooms/', views.visit_rooms, name='visit_rooms'),
]