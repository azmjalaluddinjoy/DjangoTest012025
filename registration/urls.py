from django.contrib import admin
from django.urls import path
from registration import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.machine),
    path('wlcm/',views.machine),
    # path('dl/',views.deep_learning),
    # path('about/',views.about_us),
    
]
   