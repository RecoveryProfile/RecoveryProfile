from django.shortcuts import render, redirect
from .models import GoodThingThatHappened
from django.contrib.auth.models import User
from django.http import HttpResponse

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
     
def delete_good_thing_that_happened(request): 
    good_thing = GoodThingThatHappened.objects.get(pk=request.POST['id'])
    if not (good_thing.who_its_about == request.user or good_thing.author == request.user):
        return HttpResponse('failure')
    good_thing.delete()
    
    return HttpResponse('success')
    
    save_good_thing_edit
    
def save_good_thing_edit(request): 
    good_thing = GoodThingThatHappened.objects.get(pk=request.POST['id'])
    if not (good_thing.who_its_about == request.user or good_thing.author == request.user):
        return HttpResponse('failure')
    good_thing.what_happened = request.POST['edit']
    good_thing.save()
    
    return HttpResponse('success')