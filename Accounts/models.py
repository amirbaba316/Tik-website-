from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    bio=models.TextField(max_length=150,blank=True)
