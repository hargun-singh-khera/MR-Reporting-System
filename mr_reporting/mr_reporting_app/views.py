from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserMaster
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.method == "POST":
        # username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if not UserMaster.objects.filter(email=email).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login')
        # print("Username:", username)
        print("Email:", email)
        print("\nPassword:", password)
        user = authenticate(email=email, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/form')
    else:
        return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="/login")
def redirect_url(request):
    pass
    # return render(request, 'daily_report_form.html')

@login_required(login_url="/login")
def daily_report_form(request):
    return render(request, 'detail_report_form.html')

@login_required(login_url="/login")
def areamaster_add(request):
    return HttpResponse("Area Master")
