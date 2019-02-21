from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):  #test to see if my server is up
    return HttpResponse("Testing")
#
# def