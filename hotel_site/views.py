from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Reserves


def home(request):
    return render(request, 'hotel_site/home.html')


def sign_up(request):
    return render(request, 'accounts/sign_up.html')


def my_reservations(request):
    reserves = list(Reserves.objects.filter(guest__user=request.user))
    for o in reserves:
        for o1 in list(o.reserve_item.all()):
            price = 0
            counter = 0
            for o2 in o1.staying_time.all():
                counter += 1
            price = o1.room.price * counter
            o1.total_price = price
            o1.save()
    context = {'reserves':reserves}
    return render(request, 'hotel_site/my_reservations.html', context)
