from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    offering = {'what' : 'Registration'}
    return render(request,'registration/registration.html', context=offering)
def random(request):
    return render(request,'registration/random_forest.html')
def k_nearest(request):
    return render(request,'registration/knn.html')
def dt(request):
    return render(request,'registration/dt.html')




#     return HttpResponse('')

# def deep_learning(request):
#     return HttpResponse('We have full Deep Learning course')

# def about_us(request):
#     return HttpResponse('About Us')