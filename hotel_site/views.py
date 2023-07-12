from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import *
from accounts.models import *

def home(request):
    try:
        guest = Guest.objects.get(user=request.user)
        who = "guest"
        
    except:
        try:
            staff = Staff.objects.get(user=request.user)
            if staff.role.name == "manager":
                who = "manager"
            elif staff.role.name == "housekeeper":
                who = "housekeeper"
            elif staff.role.name == "installer":
                who = "installer"
            elif staff.role.name == "receptionist":
                who = "receptionist"
            elif staff.role.name == "restaurant staff":
                who = "restaurant staff"
            else:
                who = "no one"
            
        except:
            who = "no one"
            
    context = {"who": who}
    return render(request, 'hotel_site/home.html', context)


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


def my_bill(request):
    bills = list(Bill.objects.filter(guest__user=request.user))
    context = {'bills':bills}
    return render(request, 'hotel_site/my_bills.html', context)
