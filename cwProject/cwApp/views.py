from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
from .models import Car

def index(request):  #test to see if my server is up
    return HttpResponse("Testing")

def newBook1(request): #creates new entry for book 1
    classBook1= Book(name='Moby Dick', page=927, genre='adventure-fiction',publishDate="2017-10-18")
    classBook1.save()
    return HttpResponse(classBook1)


def newBook2(request):#creates new entry for book 2
    classBook2= Book(name='Nineteen Eight-four', page=328, genre='Dystopian,political fiction',publishDate="1949-06-08")
    classBook2.save()
    return HttpResponse(classBook2)


def allBookNames (request): #returns all books
    nameofBooks=''
    totalBooks=Book.objects.all()

    for eachElement in totalBooks:
        nameofBooks+=eachElement.name + "<br>"
    return HttpResponse(nameofBooks)

#
def dateLessThan(request): #books after Jan 2,2018
    datesYounger01012018= Book.objects.filter(publishDate__gte= '2018-01-01')
    return HttpResponse(datesYounger01012018)

def newCar1(request): #create car 1
    classCar1=Car(make='Nissan',model="Altura",year="2009")
    classCar1.save()
    return HttpResponse(classCar1)


def newCar2(request): #create car 2
    classCar2=Car(make='BMW',model="3 Series Sedan",year="2016")
    classCar2.save()
    return HttpResponse(classCar2)

def allYears(request): #returns all years
    carYears=''
    totalYears=Car.objects.all()
    for eachElement in totalYears:
        carYears+=eachElement.year + '<br>'
    return HttpResponse(carYears)

def post2010(request): #returns after post 2010
    Over2010=Car.objects.filter(year__gt=2010)
    return HttpResponse(Over2010)


