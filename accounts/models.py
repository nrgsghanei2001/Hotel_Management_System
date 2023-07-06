from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guest', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username

   

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staffs')
    email = models.EmailField(blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='staffs', null=True, blank=True)

    def __str__(self):
        return self.user.username