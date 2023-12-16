from django.contrib import admin
from django.urls import path
from theapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('add',views.add),
    path('about',views.about),
    path('instructions',views.inst),
    path('developers',views.dev)
    
    
]
