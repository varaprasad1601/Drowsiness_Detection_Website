from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class register(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=250,blank=True)
    p_code = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    face_encodings = models.TextField(blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "User Register"
        

class company_register(models.Model):
    company_name = models.CharField(max_length=250,blank=True)
    manager_name = models.CharField(max_length=250,blank=True)
    company_location = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.company_name)
    
    class Meta:
        verbose_name_plural = "Company Register"
    