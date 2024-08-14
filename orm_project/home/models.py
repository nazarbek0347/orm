from django.db import models

# Create your models here.

class Register(models.Model):
    nickname=models.CharField(max_length=16,blank=False)
    name=models.CharField(max_length=200,blank=False)
    password=models.CharField(max_length=200,blank=False)
    
    def __str__(self):
        return self.nickname