from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
     path('', views.login_form, name='home'),
     path('login/', views.loginView, name='login'),
     path('regform/', views.register_form, name='regform'),
     path('register/', views.registerView, name='register'),
     
      # Publisher URL's
     path('client/', views.client, name='client'),

]



