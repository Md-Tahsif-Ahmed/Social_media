from django.urls.conf import path
from App_post import views
from django.urls import path


app_name = 'App_post'



urlpatterns = [  
     path("", views.home, name='home'),
     path('liked/<pk>', views.liked, name='liked'),
     path('unliked/<pk>', views.unliked, name='unliked'),

]