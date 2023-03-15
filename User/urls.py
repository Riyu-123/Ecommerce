from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('registersuccess/', views.registersuccess, name="registersuccess"),
    path('wishlist/', views.wishlist, name="wishlist"),
    
]