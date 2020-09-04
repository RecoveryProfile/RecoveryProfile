from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .models import ToDoList, Item
from good_things_that_happened.models import GoodThingThatHappened
from .models import ProfileAccess
from django.contrib.auth.models import User

def profile_for_self(request):
    context = {'good_things_that_happened': GoodThingThatHappened.objects.filter(who_its_about=request.user).order_by('-created_at')}
    context['profiles_you_can_acccess'] = ProfileAccess.objects.filter(access_for=request.user)
    context['is_for_self'] = True
    context['who_can_access'] = ProfileAccess.objects.filter(profile_for=request.user)
    context['following_users_good_things'] = GoodThingThatHappened.objects.filter(who_its_about__in=ProfileAccess.objects.filter(access_for=request.user).values('access_for')).order_by('-created_at')
    return render(request, "profiles/profile.html", context)
    
def profile_for_other(request, username):
    profile_for = User.objects.get(username=username)
    if not request.user.is_authenticated:
        return redirect('/login')
    can_access = ProfileAccess.objects.filter(profile_for=profile_for, access_for=request.user)
    if not can_access:
        return HttpResponse('Access denied')
    context = {'good_things_that_happened': GoodThingThatHappened.objects.filter(who_its_about=profile_for).order_by('-created_at')}
    context['profile_for'] = profile_for
    context['profiles_you_can_acccess'] = ProfileAccess.objects.filter(access_for=request.user)
    context['who_can_access'] = ProfileAccess.objects.filter(profile_for=profile_for)
    context['is_for_self'] = False
    return render(request, "profiles/profile.html", context)    
    
def add_user_who_can_access_your_profile(request):
    profile_access = ProfileAccess(profile_for=request.user, access_for=User.objects.get(username=request.POST.get('add_username')))
    profile_access.save()
    return redirect('/profile')