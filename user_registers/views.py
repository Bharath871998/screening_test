from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home.html")




def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username exists please try new user name")
                return redirect("user_register")
            else:
                messages.info(request, "Password is matching")
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('/')
        else:
            messages.info(request, "Password is not matching")
            return redirect("user_register") 
    else:
        return render(request, "user_register.html")
    
    
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = auth.authenticate(request, username = username, password = password)
        if user_auth is not None:
            auth.login(request, user_auth)
            messages.info(request, "User logged in successfully")
            return redirect('/')
        else:
            messages.info(request, "Invalid details please try again")
            return redirect("login")
    else:
        return render(request, 'login.html')
    
    
    
def logout(request):
    auth.logout(request)
    return redirect("/")
            

