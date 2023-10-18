from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import subprocess
from .models import entrydetails


# Create your views here.

def Home(request):
    return render(request,'local/Home.html')








def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('passcode')  # Corrected the variable name
        user = authenticate( username=username, password=password)
        print(user)  # Corrected the function call

        if user is not None:
            login(request, user)
            return redirect('Home')  # Make sure 'Home' is a valid URL name in your project's URL configuration
        else:
            form = AuthenticationForm()
            messages.error(request, "Wrong username or password")
            return render(request,'/signin.html')

    else:
        form = AuthenticationForm()
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



def capture_image_view(request):
    if request.method == 'POST':
        script_path = r'local/webcamcampute.py'

        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            print('nasu')
            json_data = result.stdout  # This assumes your script returns JSON data

            # Assuming you have a model for user features and you're using Django's built-in User model
            if request.user.is_authenticated:
                print('kari')
                user = request.user
                user_profile = entrydetails.objects.get(user=user)  # Replace UserProfile with your profile model
                user_profile.features = json_data
                user_profile.save()
            else:
                pass

            return render(request, 'local/Home.html')
        except Exception as e:
            # Handle the exception appropriately, e.g., log it for debugging
            return render(request, 'local/Home.html', {'error_message': str(e)})

    return render(request, 'local/Home.html')










def mark(request):
    return HttpResponse("this is the Home page")

def checkattendence(request):
    return HttpResponse("this is the Home page")

def about(request):
    return HttpResponse("this is the Home page")