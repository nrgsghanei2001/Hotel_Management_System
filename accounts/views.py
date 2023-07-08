from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import *



def sign_up(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'accounts/sign_up.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user2 = User.objects.get(username=user)
            guest = Guest.objects.create(user=user2, email=email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'accounts/sign_up.html', context)

    return render(request, 'accounts/sign_up.html', {})


def profile(request):
    try:
        guest = Guest.objects.get(user=request.user)
        staff = 'no'
    except:
        guest = Staff.objects.get(user=request.user)
        staff = 'yes'
    context = {'guest':guest,
    'staff':staff,}
    return render(request, 'accounts/profile.html', context)


def add_staff(request):
    if request.method == 'POST'  and request.is_ajax():
        text = request.POST
        username = text['username']
        email = text['email']
        password = text['password']
        role = text['role']
        role = Role.objects.get(name=role)
        user2 = User.objects.create(username=username, email=email, password=password)
        staff = Staff.objects.create(user=user2, email=email, role=role)
        staff.save()
        return JsonResponse({"text":text})
    
    roles = Role.objects.all()
    context = {'roles' : roles}
    return render(request, 'accounts/add_staff.html', context)
