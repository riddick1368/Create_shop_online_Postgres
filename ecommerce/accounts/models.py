from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100,help_text='plz enter ur name ',blank=False)
    email = models.EmailField(blank=False)
    subject = models.TextField(max_length=500,help_text="plz be short ",blank=False)
