# Create your views here.
from django.shortcuts import render, redirect

def register(request):
    return render(request, 'register.djhtml')
