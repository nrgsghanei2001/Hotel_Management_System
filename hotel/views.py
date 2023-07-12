from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden

from .models import *


def visit_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'hotel/visit_rooms.html', context)


def visit_rooms_capacity(request):
    rooms = Room.objects.all().order_by('capacity')
    context = {'rooms':rooms}
    return render(request, 'hotel/visit_rooms_capacity.html', context)


def visit_rooms_price(request):
    rooms = Room.objects.all().order_by('price')
    context = {'rooms':rooms}
    return render(request, 'hotel/visit_rooms_price.html', context)



def reserve_room(request, pk):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        number = int(text['number'])
        month = text['month']
        day = text['day']
        months = calender.Months
        for i in months:
            if i[1] == month:
                month = int(i[0])
        days = calender.Days
        for i in days:
            if i[1] == day:
                day = int(i[0])
        # print(day, month)
        reserve_dates = []
        for i in range(number):
            if day > 30:
                day = day % 30
                month += 1
            d = calender.objects.create(month=str(month), day=str(day))
            reserve_dates.append(d)
            day += 1
        reserve_items = reserve_item.objects.filter(room__pk=pk)
        reserved_stay_times = []
        for o in reserve_items:
            for o1 in o.staying_time.all():
                reserved_stay_times.append(o1)
        flag_conflict = False
        for o in reserved_stay_times:
            for o2 in reserve_dates:
                if o.day == o2.day and o.month == o2.month:
                    flag_conflict = True
                    break
        print(flag_conflict)
        if not flag_conflict:
            room = Room.objects.get(pk=pk)
            price = room.price
            # print(price)
            item = reserve_item.objects.create(room = room)
            counter = 0
            for o in reserve_dates:
                item.staying_time.add(o)
                counter += 1
            price *= counter
            print(price)
            item.total_price = price
            item.save()
            guest = Guest.objects.get(user=request.user)
            try:
                reserve = Reserves.objects.get(guest=guest)
            except:
                reserve = Reserves.objects.create(guest=guest)
            reserve.reserve_item.add(item)
            reserve.save()
            b_i = bill_item.objects.create(item="4", cost=price, status="u", 
            details=f"reserve room {room.room_number} for {counter} nights.")
            try:
                bill = Bill.objects.get(guest=guest)
            except:
                bill = Bill.objects.create(guest=guest)
            
            print(price)
            bill.bill_item.add(b_i)
            bill.total_price += price
            bill.save()
        else:
            error = "no"

        return JsonResponse({})

    room = Room.objects.get(id=pk)
    months = calender.Months
    days = calender.Days
    month = []
    for m in months:
        month.append(m[1])
    day = []
    for m in days:
        day.append(m[1])
    context = {'room':room, 'months': month, 'days': day}
    return render(request, 'hotel/reserve_room.html', context)


def service(request):
    return render(request, 'hotel/service.html')