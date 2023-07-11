from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
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


def visit_rooms_status(request):
    rooms = Room.objects.filter(availability=True)
    context = {'rooms':rooms}
    return render(request, 'hotel/visit_rooms_status.html', context)


def service(request):
    return render(request, 'hotel/service.html')

def request_installation(request):
    return render(request, 'hotel/request_installation.html')