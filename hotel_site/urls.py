from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('cancle/reserve/', views.cancle_reserve, name='cancle_reserve'),
    path('my_bill/', views.my_bill, name='my_bill'),
    path('pay_bill/', views.pay_bill, name='pay_bill'),
    path('confirm_pay/', views.confirm_pay, name='confirm_pay'),
]