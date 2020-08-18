# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import ToDoList, Item

def home(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    return render(request, "recoveryprofile/home.html", {})
