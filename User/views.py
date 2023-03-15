from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def registersuccess(request):
    return render(request, 'registersucces.html')

def wishlist(request):
    return render(request, 'wishlist.html')
