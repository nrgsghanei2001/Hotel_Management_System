from django.db import models
from django.http import JsonResponse
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, TemplateView, detail
from rest_framework import generics, viewsets, permissions, response, status
from rest_framework.views import APIView


def home_page(request):
    return render(request, 'hotel_management/home.html')


def signup_choice(request):
    return render(request, 'accounts/signup_choice.html')