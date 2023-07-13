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
    path('request_installation/', views.request_installation, name='request_installation'),
    path('request_result/', views.create_request, name='create_request'),
    path('manage_installation/', views.manage_installation, name = 'manage_installation'),
    path('ins_req_result/', views.ins_req_result, name='ins_req_result'),
    path('update_req_result/', views.update_result_ins, name='update_result_ins'),
    path('request_housekeeping/', views.request_housekeeping, name='request_housekeeping'),
    path('request_result_hk/', views.create_request_hk, name='create_request_hk'),
    path('manage_housekeeping/', views.manage_housekeeping, name = 'manage_housekeeping'),
    path('hk_req_result/', views.hk_req_result, name='hk_req_result'),
    path('update_req_result_hk/', views.update_result_hk, name='update_result_hk'),
    path('service/food/', views.service_food, name='service_food'),
    path('food_request/', views.food_request, name='food_request'),
    path('menu/', views.menu, name='menu'),
    path('internet/', views.internet, name='internet')
]
