from django.shortcuts import render
from django.contrib import messages
from customers.forms import RegisterForm
from hotel_site.urls import *
from .models import *
from django.contrib.auth.models import User



def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register_staff.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user2 = User.objects.get(username=user)
            Staff.objects.create(user=user2, email=email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register_staff.html', context)

    return render(request, 'register_staff.html', {})