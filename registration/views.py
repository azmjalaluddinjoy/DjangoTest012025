from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    return render(request,'registration.html')

#     return HttpResponse('')

# def deep_learning(request):
#     return HttpResponse('We have full Deep Learning course')

# def about_us(request):
#     return HttpResponse('About Us')