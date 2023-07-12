from django.urls import path
from . import views


urlpatterns = [
    path('visit_rooms/', views.visit_rooms, name='visit_rooms'),
    path('visit_rooms/capacity/', views.visit_rooms_capacity, name='visit_rooms_capacity'),
    path('visit_rooms/price/', views.visit_rooms_price, name='visit_rooms_price'),
    path('visit_rooms/<int:pk>', views.reserve_room, name='reserve_room'),
    path('service/', views.service, name='service'),
    path('add_room/', views.add_room, name='add_room'),
    path('all_rooms/', views.all_rooms, name='all_rooms'),
]