from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    subscription_validity = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save
    

    def is_subscribed(self):
        return datetime.datetime.now(datetime.timezone.utc) <  self.subscription_validity
         

    def get_subscription_validity(self):
        if self.is_subscribed:
            duration = self.subscription_validity - datetime.datetime.now(datetime.timezone.utc)  
            return duration.days 
        else:
            return 0