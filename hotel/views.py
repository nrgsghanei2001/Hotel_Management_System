from django.shortcuts import render, redirect
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


def add_room(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        room_number = int(text['room_number'])
        capacity = int(text['capacity'])
        price = float(text['price'])
        room = Room.objects.create(room_number=room_number, capacity=capacity, price=price)
        room.save()
        return JsonResponse({"text":text})
    
    return render(request, 'hotel/add_room.html')


def all_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'hotel/all_rooms.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    reserve_items = reserve_item.objects.filter(room__pk=pk)
    for o in reserve_items:
        o.delete()
    room.delete()
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'hotel/all_rooms.html', context)


def cancle_reserve_manager(request, pk):
    item = reserve_item.objects.get(pk=pk)
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

    reserves = Reserves.objects.all()
    context = {'reserves':reserves}
    return redirect("all_reserves")
    # return render(request, 'hotel/all_reserves.html', context)


def all_reserves(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        username = text['username']
        reserve = Reserves.objects.get(guest__user__username=username)
        counter = 1
        context = {}
        for i in reserve.reserve_item.all():
            y = " , ".join(f"{s.month}/{s.day}" for s in i.staying_time.all())
            x = {'room':i.room.room_number, 'price':i.total_price, 'staying_time': y, 'pk': i.pk}
            key = str(counter)
            context[key] = x
            counter += 1
        return JsonResponse(context)

    reserves = Reserves.objects.all()
    context = {'reserves':reserves}
    return render(request, 'hotel/all_reserves.html', context)


def service(request):
    return render(request, 'hotel/service.html')