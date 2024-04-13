from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserMaster
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime

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
    # pass
    return redirect('/form')


@login_required(login_url="/login")
def areamaster_add(request):
    return HttpResponse("Area Master")


@login_required(login_url="/login")
def daily_report_form(request):
    employees = UserMaster.objects.filter(is_superuser=False)
    employee_id = request.GET.get('employee', None)
    month_name = request.GET.get('month', None)
    print("Month ID: ", month_name)
    months = None
    employee_selected = False
    month_selected = False
    showTable = False
    tour_program = None
    if employee_id and employee_id.isdigit():
        tour_program = TourProgram.objects.filter(employee_id=employee_id)
        months = set(program.date_of_tour.strftime('%B') for program in tour_program)
        employee_selected = True
        print(months)
        
    if month_name:
        selected_month = datetime.strptime(month_name, '%B').month
        tour_program = tour_program.filter(date_of_tour__month=selected_month)
        month_selected = True
        print("Month: " + month_name)
    if employee_selected and month_selected:
        showTable = True

    context = {
        'employees': employees,
        'employee_id': employee_id,
        'tour_program': tour_program,
        'months': months,
        'showTable': showTable,
    }
    return render(request, 'daily_report_form.html', context)


@login_required(login_url="/login")
def daily_report_form_detail(request):
    employees = UserMaster.objects.filter(is_superuser=False)
    employee_id = request.GET.get('employee', None)
    employee_designation = None
    tour_program = None
    if employee_id and employee_id.isdigit():
        employee_designation = UserMaster.objects.get(id=employee_id)
        tour_program = TourProgram.objects.get(id=employee_id)
    context = {
        'employees': employees,
        'employee_designation': employee_designation,
        'tour_program': tour_program,
    }
    return render(request, 'daily_report_form_detail.html', context)



@login_required(login_url="/login")
def report(request):
    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)
    state = None
    city = None
    if countryid:
        getcountry = CountryMaster.objects.get(id=countryid)
        state = StateMaster.objects.filter(country=getcountry)
    if stateid:
        getstate = StateMaster.objects.get(id=stateid)
        city = CityMaster.objects.filter(state=getstate)
    country = CountryMaster.objects.all()
    context = {
        'country': country,
        'state': state,
        'city': city
    }
    return render(request, 'report.html', context)