from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # auth.authenticate checks whether the username and password is mathces or not in databse
        user = auth.authenticate(username=username, password=password)

        if user is not None:  # if we get user iinfo
            auth.login(request, user)
            # format string go through geeksforgeeks python output formatting
            messages.success(request, f"You are logged in as {user}")
            return redirect('dashboard')

        else:  # if we don't get then error
            messages.error(request, 'invlaid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # right username is already a field given by djngo User class automatically and left username is we are grabing from up...and if it exists same useraname it will give error
            if User.objects.filter(username=username).exists():
                # formating string f
                messages.error(request, f' {username} username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'{email} email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    messages.success(
                        request, f'{username} : Account created successfully')
                    return redirect('login')

        else:
            messages.error(request, 'Password do not match')
            # if password doesnot match then we will redirect it to register url
            return redirect('register')

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')


# Login url is if we bychance visit dashboard then he must login first gets redirected in login
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
