from django.contrib import admin
from django.urls import path, include, re_path
from register import views as v
from recoveryprofile import views as rpviews
from profiles import views as profileviews
from good_things_that_happened import views as good_things_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path("", rpviews.home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('profile/', profileviews.profile_for_self),
    path('add_good_thing_that_happened_to_self/', good_things_views.add_good_thing_that_happened_to_self),
    path('add_good_thing_that_happened_to_other/', good_things_views.add_good_thing_that_happened_to_other),
    re_path('profiles/(?P<username>\w+)/', profileviews.profile_for_other),
    path('add_user_who_can_access_your_profile/', profileviews.add_user_who_can_access_your_profile),
]

