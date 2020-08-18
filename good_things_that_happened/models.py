from django.db import models
from django.contrib.auth.models import User

class GoodThingThatHappened(models.Model):
    what_happened = models.TextField()
    who_its_about = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='%(class)s_who_its_about')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='%(class)s_author')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.what_happened