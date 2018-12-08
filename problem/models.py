from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.
class Problem(models.Model):
    title=models.CharField(max_length=31,unique=True)
    description=models.TextField(max_length=255,default='')
    answer=models.CharField(max_length=31)
    slug=models.SlugField(max_length=31,unique=True)
    difficulty=models.CharField(max_length=6)

    def get_absolute_url(self):
        return reverse('problem_detail',kwargs={'slug':self.slug})
