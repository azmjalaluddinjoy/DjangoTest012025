from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    return HttpResponse('Welcome to Machine Django from Joy')

def deep_learning(request):
    return HttpResponse('Welcome to Deep Learning')

def about_us(request):
    return HttpResponse('About Us')