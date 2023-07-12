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


def cancle_reserve(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        item = reserve_item.objects.get(pk=text['item'])
        reserve = item.Reserves.last()
        price = item.total_price
        room = item.room.room_number
        guest = reserve.guest
        item.delete()
        reserve.save()
        bi = Bill.objects.get(guest=guest)
        for o in bi.bill_item.all():
            if str(room) in o.details and o.cost == price:
                o.cancle = "y"
                o.save()
                break
        bi.total_price -= price
        bi.save()
        return render(request, 'hotel_site/my_reservations.html')
    return render(request, 'hotel_site/my_reservations.html')


def my_bill(request):
    bills = list(Bill.objects.filter(guest__user=request.user))
    context = {'bills':bills}
    return render(request, 'hotel_site/my_bills.html', context)


def pay_bill(request):
    bills = list(Bill.objects.filter(guest__user=request.user))
    total_price = 0
    for b in bills:
        total_price += b.total_price

    context = {'total_price':total_price}
    return render(request, 'hotel_site/bank.html', context)


def confirm_pay(request):
    bills = list(Bill.objects.filter(guest__user=request.user))
    for b in bills:
        for bi in b.bill_item.all():
            bi.status = "p"
            bi.save()
        if b.total_price > 0:
            b.total_price = 0.0
        b.save()
    bills = list(Bill.objects.filter(guest__user=request.user))
    context = {'bills':bills}
    return render(request, 'hotel_site/my_bills.html', context)


