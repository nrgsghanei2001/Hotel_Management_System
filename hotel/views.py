from django.shortcuts import render
from .models import *


def visit_rooms(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'hotel/visit_rooms.html', context)


def service(request):
    return render(request, 'hotel/service.html')