from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import KundenForm, LoginForm
from subprocess import run, PIPE
import sys

# Create your views here.


def index(response):
    return HttpResponse("<h1>test to see if this works</h1>")

def users(request):
    return render(request, "users.html")

def login(request):
    return render(request, "login.html")

def login1(request):
    form = LoginForm()
    print(request.POST)
    form = LoginForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "login1.html")

def app(request):
    return render(request, "app.component.html")

def loginattempt(request):
    data=request.get("")
    print(data.text)
    data=data.text
    return render(request, 'menu.html', {'data':data})

def external(request):
    inp= request.POST.get('param')

    out= run(sys.executable,['location.py', inp], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'index.html',{'data':out.stdout})

def register(request):
    form = KundenForm()

    if request.method == 'POST':
        print(request.POST)
        form = KundenForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    #daten = {
    #    "benutzername": benutzername,
    #    "vorname": vorname,
    #    "nachname": nachname,
    #    "email": email,
    #    "passwort": passwort
    #}

    #data = [{{form.benutzername}}, {{form.vorname}}, {{form.nachname}}, {{form.email}}, {{form.passwort}}]
    #print(data)
    

    return render(request, 'registration.html', context)

def createevents(request):

    if request.method == 'POST':
        print("success")

    return render(request, 'events.html')