from django.db import models
from django.http import HttpResponse

# Create your models here.
class signin(models.Model):
    name = models.TextField(max_length=20)
    password = models.TextField(max_length=30)
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return f"{self.name,self.password,self.email}"
    

    
    
    
    
    

    