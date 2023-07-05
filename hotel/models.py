from django.db import models
from django.contrib.auth.models import User


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
