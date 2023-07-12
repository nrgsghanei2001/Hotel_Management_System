from django.urls import path
from . import views


urlpatterns = [
    path('visit_rooms/', views.visit_rooms, name='visit_rooms'),
    path('visit_rooms/capacity/', views.visit_rooms_capacity,
         name='visit_rooms_capacity'),
    path('visit_rooms/price/', views.visit_rooms_price, name='visit_rooms_price'),
    path('visit_rooms/status/', views.visit_rooms_status,
         name='visit_rooms_status'),
    path('service/', views.service, name='service'),
    path('service/food/', views.service_food, name='service_food'),
    path('food_request/', views.food_request, name='food_request')
]
