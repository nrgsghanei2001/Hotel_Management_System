from django.urls import path
from .views import *
from django.urls.conf import include, include
from django.conf import settings
from django.conf.urls.static import static
import os
from rest_framework import routers


urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('profile/', profile, name='profile'),
    path('add_staff/', add_staff, name='add_staff'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + os.path.altsep)