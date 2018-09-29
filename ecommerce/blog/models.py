from django.db import models

# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=120,unique=True,blank=False,null=False)
    slug = models.SlugField()
    description = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.title


