from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):  #Book model
    name=models.CharField(max_length=250)
    pageNumber=models.IntegerField()
    genre=models.CharField(max_length=30)
    publishDate=models.DateField(default=timezone.now())

    def __str__(self):  #names each book to read easier
        return self.name

class Car (models.Model):  #Car model
    make=models.CharField(max_length=60)
    model=models.CharField(max_length=60)
    year=models.IntegerField()

    def __str__(self): #names each car to name easier
        return self.make
