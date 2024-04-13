from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserMaster
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from django.db import transaction



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
    date = request.GET.get('date')
    source_area = request.GET.get('from')
    destination_area = request.GET.get('to')
    employee_designation = None
    tour_program = None
    employee_designation = UserMaster.objects.get(id=employee_id)
    tour_program = TourProgram.objects.filter(employee_id=employee_id)
    doctors = None
    stockists = None
    gifts = GiftMaster.objects.all()
    units = UnitMaster.objects.all()
    products = ProductMaster.objects.all()

    if destination_area:
        destination_area_name = AreaMaster.objects.get(area=destination_area)
        destination_area_id = destination_area_name.id
        doctors = DoctorMaster.objects.filter(area_id=destination_area_id)
        stockists = StockistMaster.objects.filter(area_id=destination_area_id)

    if request.method == "POST":
        employee_name = request.POST.get('employee_name')
        emp_designation = request.POST.get('employee_designation')
        date_of_working = request.POST.get('date_of_working')
        emp_source_area = request.POST.get('source_area')
        emp_destination_area = request.POST.get('destination_area')
        doctor_name = request.POST.get('doctor')
        doctor_departure_time = request.POST.get('doctor_departure_time')
        doctor_arrival_time = request.POST.get('doctor_arrival_time')
        product_name = request.POST.get('product')
        product_unit = request.POST.get('product_unit')
        product_qty = request.POST.get('product_qty')
        gift = request.POST.get('gift')
        gift_unit = request.POST.get('gift_unit')
        gift_qty = request.POST.get('gift_qty')
        stockist = request.POST.get('stockist')
        stockist_departure_time = request.POST.get('stockist_departure_time')
        stockist_arrival_time = request.POST.get('stockist_arrival_time')

        employee_id = UserMaster.objects.get(name=employee_name)
        source_area_id = AreaMaster.objects.get(area=emp_source_area)
        destination_area_id = AreaMaster.objects.get(area=emp_destination_area)
    
        doctor_id = DoctorMaster.objects.get(id=int(doctor_name))

        product_id = ProductMaster.objects.get(id=int(product_name))
        product_unit_id = UnitMaster.objects.get(id=int(product_unit))
        gift_id = GiftMaster.objects.get(id=int(gift))
        gift_unit_id = UnitMaster.objects.get(id=int(gift_unit))
        stockist_id = StockistMaster.objects.get(id=int(stockist))
       
        print("Doctor Name:",  doctor_name)
        print("Doctor Id:", doctor_id, "Product Id:", product_id, "Product Unit Id:", product_unit_id, "Gift Id:", gift_id, 
              "Gift Unit Id:", gift_unit_id, "Stockist Id:", stockist_id)

        # data = DailyReporting(
        #     employee=employee_id,
        #     designation=emp_designation,
        #     date_of_working=date_of_working,
        #     source_area=source_area_id,
        #     destination_area=destination_area_id,
        #     doctor=doctor_id,
        #     doctor_time_in=doctor_arrival_time, 
        #     doctor_time_out=doctor_departure_time, 
        #     product=product_id,
        #     product_unit_id=product_unit,
        #     product_quantity=product_qty,
        #     gift=gift_id, 
        #     gift_unit_id=gift_unit,
        #     gift_quantity=gift_qty,
        #     stockist=stockist_id, 
        #     stockist_time_in=stockist_arrival_time, 
        #     stockist_time_out=stockist_departure_time
        # )
        # data.save()


        print("POST executed")

        print("Employee Name:", employee_name, "Employee Designation:", emp_designation, "Date of Working:", date_of_working, 
              "Employee Source Area:", emp_source_area, "Employee Destination Area:", emp_destination_area)
        print("Doctor name:", doctor_name, "Arrival Time:", doctor_arrival_time, "Departure Time:", doctor_departure_time)
        print("Product Name:", product_name, "Product Unit:", product_unit, "Product Qty:", product_qty)
        print("Gift Name:", gift, "Gift Unit:", gift_unit, "Gift Qty:", gift_qty)
        print("Stockist Name:", stockist, "Arrival Time:", stockist_arrival_time, "Departure Time:", stockist_departure_time)
        return redirect('daily_report_form')
    
    context = {
        'employees': employees,
        'employee_id': employee_id,
        'employee_designation': employee_designation,
        'tour_program': tour_program,
        'date': date,
        'source_area': source_area,
        'destination_area': destination_area,
        'doctors': doctors,
        'stockists': stockists,
        'gifts': gifts,
        'units': units,
        'products': products,
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