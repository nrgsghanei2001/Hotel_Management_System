from django.contrib import admin
from .models import *



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['users', 'email']
    list_editable = ['email']

    @admin.display(description='user')
    def users(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return obj.device
