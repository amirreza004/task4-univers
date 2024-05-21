from django.db import models

# Create your models here.

class profile(models,Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=20)
    summary=models.TextField(max_length=250 , editable=True)
    skills=models.ImageField()
    experience=models.TextField()
    education=models.TextField()



