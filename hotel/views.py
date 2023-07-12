from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import *
from django.db.models import Q
import datetime


def get_room_number(request):
    reserves = list(Reserves.objects.filter(guest__user=request.user))
    roomNumber = None
    for obj in reserves:
        for obj2 in obj.reserve_item.all():
            for obj3 in list(obj2.staying_time.all()):
                d1 = '{d.month}/{d.day}'.format(d=datetime.datetime.now())
                if (d1 == str(obj3)):
                    roomNumber = obj2.room.room_number
                    return roomNumber
    return roomNumber


def visit_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'hotel/visit_rooms.html', context)


def visit_rooms_capacity(request):
    rooms = Room.objects.all().order_by('capacity')
    context = {'rooms': rooms}
    return render(request, 'hotel/visit_rooms_capacity.html', context)


def visit_rooms_price(request):
    rooms = Room.objects.all().order_by('price')
    context = {'rooms': rooms}
    return render(request, 'hotel/visit_rooms_price.html', context)


def visit_rooms_status(request):
    rooms = Room.objects.filter(availability=True)
    context = {'rooms': rooms}
    return render(request, 'hotel/visit_rooms_status.html', context)


def service(request):
    return render(request, 'hotel/service.html')


def service_food(request):
    if (get_room_number(request) == None):
        return render(request, 'hotel/no_room.html')

    email = request.user.email
    if request.method == "POST":
        current = Order.objects.filter(email=email).get(status=0)
        type = request.POST.get('type')
        if (type == '0'):
            name = request.POST.get('name')
            price = int(request.POST.get('price'))
            food_obj = Food.objects.get(name=name)
            if (food_obj.quantity > 0):
                food_obj.quantity -= 1
                current.food_list += name + '#'
                current.price += price
                food_obj.save()
        else:
            current.status = 1
        current.save()

    current = Order.objects.filter(email=email).filter(status=0)
    if (len(current) == 0):
        mx = Order.objects.latest('id')
        current = Order(food_list="", price=0,
                        email=email, status=0, id=mx.id + 1)
        current.save()
    else:
        current = current[0]

    food_list = current.food_list.split('#')[:-1]
    foods = Food.objects.all
    return render(request, 'hotel/service_food.html', {'foods': foods, 'food_list': food_list})


def food_request(request):
    if request.method == "POST":
        type = request.POST.get('type')
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.status = 2
        order.save()
    orders = Order.objects.filter(status=1).filter(~Q(price=0))
    return render(request, 'hotel/food_request.html', {'orders': orders})


def menu(request):
    if request.method == "POST":
        type = request.POST.get('type')
        name = request.POST.get('name')
        price = int(request.POST.get('price'))
        quantity = int(request.POST.get('quantity'))
        if (type == '0'):
            food = Food.objects.filter(name=name).filter(
                price=price).get(quantity=quantity)
            food.delete()
        else:
            food = Food(name=name, price=int(price), quantity=int(quantity))
            food.save()

    foods = Food.objects.all
    return render(request, 'hotel/menu.html', {'foods': foods})


def internet(request):
    if (get_room_number(request) == None):
        return render(request, 'hotel/no_room.html')
    email = request.user.email
    account = InternetAccount.objects.filter(email=email)
    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if (password1 != "" and password1 == password2):
            if (len(account) == 0):
                account = InternetAccount(
                    email=email, password=password1)
            else:
                account = account[0]
                account.password = password1
            account.save()

    account = InternetAccount.objects.filter(email=email)
    has = "1"
    if (len(account) == 0):
        account = None
        has = "0"
    else:
        account = account[0]

    return render(request, 'hotel/internet.html', {'account': account, 'has': has})
