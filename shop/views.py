from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("Hello buddy you are about page")

def tracker(request):
    return HttpResponse("Hello buddy you are in tracker page")

def login(request):
    return HttpResponse("Hello buddy you are in login page")

def contact(request):
    return HttpResponse("Hello buddy you are in contact page")

def search(request):
    return HttpResponse("Hello buddy you are in search page")

def prodView(request):
    return HttpResponse("Hello buddy you are product view")

def checkout(request):
    return HttpResponse("Hello buddy you are in checkout page")
