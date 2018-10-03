from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    image = models.ImageField()
    website = models.URLField()



class Post (models.Model):
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=120,unique=True,blank=False,null=False)
    slug = models.SlugField()
    description = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.title


