from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    file = models.FileField(upload_to="resumes")
    resumeid = models.CharField(max_length=10)
    def __str__(self):
        return ( f'{self.user.username} { "--active" if self.active else " " }')
        
class Video(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    preference = models.PositiveSmallIntegerField(blank=True, null=True)
    file = models.FileField(upload_to="video")
    