from django.db import models


class Room(models.Model):
    room_number = models.IntegerField(null=False, blank=False, unique=True)
    capacity = models.IntegerField(null=False, blank=False)
    availability = models.BooleanField(null=True, blank=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.room_number)
