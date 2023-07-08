from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'hotel_site/home.html')


def sign_up(request):
    return render(request, 'accounts/sign_up.html')

