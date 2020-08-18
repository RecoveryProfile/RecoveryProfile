from django.db import models
from django.contrib.auth.models import User

class ProfileAccess(models.Model):
    profile_for = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='%(class)s_who_its_about')
    access_for = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='%(class)s_author')

    def __str__(self):
         return '%s %s' % (self.profile_for.username, self.access_for)