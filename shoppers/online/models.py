from django.db import models

# Create your models here.

class sales(models.Model):
    name= models.CharField(max_length=100, default=False)
    email=models.EmailField()
    age=models.IntegerField()
    image=models.ImageField(upload_to= 'image', default='profile.png')
