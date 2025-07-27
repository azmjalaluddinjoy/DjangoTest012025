from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog1(request0):
    return HttpResponse('<p> This is our first blog<p>')
