from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# My Index
def index(request):
    return render(request, "index.html")

def helloworld(request):
    return render(request, "hello_world.html")