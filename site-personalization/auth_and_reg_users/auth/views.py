from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



def home(request):
    return render(
        request,
        'home.html'
    )


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(
        request,
        'signup.html',
        {'form': form}
    )


def login_view(request):
    template = "login.html"
    context={}
    return render(
        request,
        template,
        context)

def logout_view(request):
    logout(request)
    template = "logged_out.html"
    return render(
        request,
        template
    )