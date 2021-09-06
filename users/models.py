from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pictures', default=os.path.join('pictures', 'comic_c.jpg'))


    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height < 200 or img.width > 200:
             img.thumbnail((200, 200))
             img.save(self.profile_pic.path)
