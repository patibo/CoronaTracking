from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(response):
    return HttpResponse("<h1>test to see if this works</h1>")

def users(request):
    return render(request, "users.html")

def login(request):
    return render(request, "login.html")

def app(request):
    return render(request, "app.component.html")

def loginattempt(request):
    data=request.get("")
    print(data.text)
    data=data.text
    return render(request, 'menu.html', {'data':data})