from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'capacity', 'price']
    list_display_links = ['room_number']


@admin.register(calender)
class calenderAdmin(admin.ModelAdmin):
    list_display = ['month', 'day']


@admin.register(reserve_item)
class reserveItemAdmin(admin.ModelAdmin):
    list_display = ['room', 'time', 'total_price']

    @admin.display(description='staying time')
    def time(self, obj):
        return "room "+str(obj.room.room_number) + " days:" + " , ".join(f"{s.month}/{s.day}" for s in obj.staying_time.all())


@admin.register(Reserves)
class reservesAdmin(admin.ModelAdmin):
    list_display = ['Guest', 'Reserves']

    @admin.display(description='Guest')
    def Guest(self, obj):
        return obj.guest.user.username

    @admin.display(description='Reserves')
    def Reserves(self, obj):
        return " , ".join(r.item_name() for r in obj.reserve_item.all())


@admin.register(Food)
class foodAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price']


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['food_list', 'price', 'id', 'email', 'status', 'Date']
