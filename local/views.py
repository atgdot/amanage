from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'local/index.html')

def login(request):
    return render(request, 'local/login.html')

def upload(request):
    return render(request, 'local/index.html')

def mark(request):
    return render(request, 'local/index.html')

def checkattendence(request):
    return render(request, 'local/index.html')

def about(request):
    return render(request, 'local/index.html')