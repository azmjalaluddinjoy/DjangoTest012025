
from django.urls import path
from . import views

urlpatterns = [
    path('wlcm/',views.machine),
    path('dl/',views.deep_learning),
    path('about/',views.about_us),
    
]
   