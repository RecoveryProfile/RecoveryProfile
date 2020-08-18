from django.shortcuts import render, redirect
from .models import GoodThingThatHappened
from django.contrib.auth.models import User

def add_good_thing_that_happened_to_self(request):
     what_happened = request.POST.get('what_happened')
     print('what happened', what_happened)
     good_thing_obj = GoodThingThatHappened(what_happened=what_happened, who_its_about=request.user,  author=request.user)
     good_thing_obj.save()
     return redirect('/profile')
     
def add_good_thing_that_happened_to_other(request):
     profile_for = User.objects.get(username=request.POST.get('profile_for'))
     what_happened = request.POST.get('what_happened')
     print('what happened', what_happened)
     good_thing_obj = GoodThingThatHappened(what_happened=what_happened, who_its_about=profile_for,  author=request.user)
     good_thing_obj.save()
     return redirect('/profiles/'+profile_for.username)     
