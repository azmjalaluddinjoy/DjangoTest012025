from django.contrib import admin
from django.urls import path
from registration import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.machine),
    path('wlcm/',views.machine),
    path('rn/',views.random),
    path('knn/',views.k_nearest),
    path('dt/',views.dt),
    # path('dl/',views.deep_learning),
    # path('about/',views.about_us),
    
]
   