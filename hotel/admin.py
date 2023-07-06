from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'capacity', 'availability', 'price']
    list_display_links = ['room_number']


