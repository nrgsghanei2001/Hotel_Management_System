from django.urls import path
from .views import *


urlpatterns = [
    path('register/guest/', register, name='register_guest'),
]