from django.db import models
from accounts.models import Guest


class Room(models.Model):
    room_number = models.IntegerField(null=False, blank=False, unique=True)
    capacity = models.IntegerField(null=False, blank=False)
    # availability = models.BooleanField(null=True, blank=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.room_number)


class calender(models.Model):
    Months = (
        ("1", 'January'), ('2', 'February'), ('3', 'March'), ('4',
                                                              'April'), ('5', "May"), ('6', "June"), ('7', "July"),
        ('8', "August"), ('9', "September"), ('10', "October"), ('11', "November"), ('12', "December"))

    Days = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
            ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14',
                                                                     '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'),
            ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23',
                                                                     '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'),
            ('28', '28'), ('29', '29'), ('30', '30'))

    month = models.CharField(max_length=2, choices=Months, default=1)
    day = models.CharField(max_length=2, choices=Days, default=1)

    def __str__(self):
        return f"{self.month}/{self.day}"


class reserve_item(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='reserve_item', null=True)
    staying_time = models.ManyToManyField(
        calender, related_name="reserve_item")
    total_price = models.FloatField(null=True, blank=True)

    def item_name(self):
        return str(self.room.room_number) + " " + " , ".join(f"{s.month}/{s.day}" for s in self.staying_time.all())

    def __str__(self):
        return str(self.room.room_number) + " " + " , ".join(f"{s.month}/{s.day}" for s in self.staying_time.all())


class Reserves(models.Model):
    guest = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="Reserves")
    reserve_item = models.ManyToManyField(
        reserve_item, related_name="Reserves")

    def item_name(self):
        return self.guest.user.username + " , ".join(r.item_name() for r in self.reserve_item.all())

    def __str__(self):
        return self.guest.user.username + " , ".join(r.item_name() for r in self.reserve_item.all())


class Food(models.Model):
    name = models.CharField()
    quantity = models.IntegerField()
    price = models.IntegerField()


class Order(models.Model):
    food_list = models.TextField(default="")
    price = models.IntegerField(default=0)
    email = models.CharField(default="")
    status = models.IntegerField(default=0)
    id = models.IntegerField(default=0, primary_key=True)
    Date = models.DateTimeField(auto_now_add=True)


class InternetAccount(models.Model):
    password = models.CharField(default="")
    email = models.CharField(default="")
