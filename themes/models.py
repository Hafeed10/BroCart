from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    bannar = models.ImageField(upload_to='media/site/')
    caption=models.TextField()