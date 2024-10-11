from django.shortcuts import render
from django.http import HttpResponse

def greet(request):
    return HttpResponse("Welcome to the server world of Django!")