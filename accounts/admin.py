from django.contrib import admin
from .models import *


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['user', 'email']
    list_editable = ['email']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'role']
    list_editable = ['email']


@admin.register(Role)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name']
