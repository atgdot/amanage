from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


# Create your views here.

def Home(request):
    return render( 'Home.html')






def signin(request):
    if request.method == "POST":
        usernow = request.POST.get('username')
        passcode = request.POST.get('username')

        user = authenticate(username=usernow, password=passcode)

        if user is not None:
            login(request, user)
            #return redirect('Home')

        else:
            messages.error(request,"wrong username or password")
            return redirect('signin')
    

    return render(request, 'local/signin.html')






def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        rollno = request.POST.get('Rollno')
        emailid = request.POST.get('emailid')
        passcode = request.POST.get('passcode')
        cpasscode = request.POST.get('cpasscode')

        myuser = User.objects.create_user(username, emailid, passcode)
        myuser.save()

        messages.success(request, "Your Account has been Successfully created.")

        return redirect('signin')
        


    return render(request, 'local/signup.html')






def mark(request):
    return HttpResponse("this is the Home page")

def checkattendence(request):
    return HttpResponse("this is the Home page")

def about(request):
    return HttpResponse("this is the Home page")