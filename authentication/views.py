from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = ''
        password = request.POST['password']
        password2 = request.POST['password2']
        token = request.POST['token']

        user = User.objects.create_user(username, email, password)
        user.token = token
        user.save()
        messages.success(request, "Your accout has been successfully created.")
        messages.success(request, "Please sign in.")
        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        token = request.POST['token']

        user = authenticate(username=username,
                            password=password, token=token)

        if user is not None:
            login(request, user)
            username = user.username
            #token = user.token

            messages.success(request, "Successfully Signed In.")
            return render(request, "authentication/dashboard.html", {'username': username, 'token': token})
        else:
            messages.error(request, "Wrong Credentials!")
            messages.error(request, "Please sign in again.")
            return redirect('signin')

    return render(request, "authentication/signin.html")


def signout(request):
    messages.error(request, "Successfully Signed Out.")
    return render(request, "authentication/signin.html")


def dashboard(request):
    return render(request, "authentication/dashboard.html")
