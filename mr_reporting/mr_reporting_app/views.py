from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserMaster
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date, datetime
from django.urls import reverse
from django.http import HttpResponseRedirect



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
        # print("User type:", request.user.is_superuser)
        user = authenticate(email=email, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login')
        elif user.is_superuser:
            messages.error(request, "Sorry!, you are not privileged to access this MR dashboard.")
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
    user = request.user
    print("User:", user)
    id = user.id
    print(id)
    employee = UserMaster.objects.get(id=id)
    print(employee)
    tour_program = TourProgram.objects.filter(employee_id=id)
    months = set(program.date_of_tour.strftime('%B') for program in tour_program)
    print(months)
    showTable = False
    month_name = request.GET.get('month', None)
    if month_name:
        selected_month = datetime.strptime(month_name, '%B').month
        tour_program = tour_program.filter(date_of_tour__month=selected_month)
        month_selected = True
        print("Month: " + month_name)
        showTable = True

    current_date = datetime.now().date()
    for tour_prgrm in tour_program:
        if tour_prgrm.submitted == False:
            if tour_prgrm.date_of_tour < current_date:
                tour_prgrm.blocked = True
                tour_prgrm.save()

    context = {
        'employee': employee,
        'employee_id':id,
        'months': months,
        'tour_program': tour_program,
        'showTable': showTable
    }
    return render(request, 'daily_report_form.html' , context)

@login_required(login_url="/login")
def submit_form(request, tour_id):
    if request.method == 'POST':
        tour_program = TourProgram.objects.get(pk=tour_id)
        tour_program.submitted = True
        tour_program.save()

    return redirect('daily_report_form')

    

@login_required(login_url="/login")
def daily_report_form_tour(request, id, tour_id):
    tour_program = TourProgram.objects.filter(id=tour_id)
    print("Tour Program:",tour_program)
    if request.method == 'POST':
        date_of_working = tour_program.get().date_of_tour
        from_area = tour_program.get().from_area
        to_area = tour_program.get().to_area
        designation = UserMaster.objects.get(id=id).designation
        print("Employee id:", id, "Date of working", date_of_working, "Source Area:", from_area, "Destination Area:",to_area)
        employee = UserMaster.objects.get(id=id)
        data = DailyReporting(
            employee=employee,
            designation=designation,
            date_of_working=date_of_working,
            source_area=from_area,
            destination_area=to_area
        )
        data.save()
        return redirect('daily_report_form_detail',id=id,tour_id=tour_id)

@login_required(login_url="/login")
def daily_report_form_detail(request,id,tour_id):
    print("Hello")
    employee_id = id
    employee = UserMaster.objects.get(id=id)
    tour_program = TourProgram.objects.get(id=tour_id)
    date = tour_program.date_of_tour
    from_area = tour_program.from_area
    to_area = tour_program.to_area
    designation = employee.designation
    area_id = AreaMaster.objects.get(area=to_area)
    print("Employee:",employee, "Date:",date, "From Area:",from_area, "To Area:",to_area, "Designation:", designation,"Area Id:", area_id)

    doctor_id = request.GET.get('doctorId', None)
    if doctor_id:
        print("Doctor Id of: ",doctor_id)
        request.session["selected_doctor_id"] = doctor_id

    gifts = GiftMaster.objects.all()
    units = UnitMaster.objects.all()
    products = ProductMaster.objects.all()
    doctors = DoctorMaster.objects.filter(area_id=area_id)
    # doctors = DoctorMaster.objects.all()
    stockists = StockistMaster.objects.filter(area_id=area_id)

    daily_reporting = DailyReporting.objects.filter(date_of_working=date).get(employee_id=id)
    print(daily_reporting)
    daily_reporting_id = daily_reporting


    doctors_in_daily_reporting = DoctorAdded.objects.filter(daily_reporting_id=daily_reporting_id).values_list('doctor__id', flat=True)
    available_doctors = doctors.exclude(id__in=doctors_in_daily_reporting)
    doctors = available_doctors

    doctor_id = request.session.get('selected_doctor_id')
    print("Session doctorid:", doctor_id)

    products_in_daily_reporting = ProductAdded.objects.filter(daily_reporting_id=daily_reporting_id).values_list('product__id', flat=True)
    available_products = products.exclude(id__in=products_in_daily_reporting)
    products = available_products

    gifts_in_daily_reporting = GiftAdded.objects.filter(daily_reporting_id=daily_reporting_id).values_list('gift__id', flat=True)
    available_gifts = gifts.exclude(id__in=gifts_in_daily_reporting)
    gifts = available_gifts

    stockist_in_daily_reporting = StockistAdded.objects.filter(daily_reporting_id=daily_reporting_id).values_list('stockist__id', flat=True)
    available_stockists = stockists.exclude(id__in=stockist_in_daily_reporting)
    stockists = available_stockists

    showSubmitWarning = True
    
    if request.method == "POST":
        if 'doctor' in request.POST and 'doctor_arrival_time' in request.POST and 'doctor_departure_time' in request.POST:
            doctor_name = request.POST.get('doctor')
            time_in = request.POST.get('doctor_arrival_time')
            time_out = request.POST.get('doctor_departure_time')
            
            doctor = DoctorMaster.objects.get(id=int(doctor_name))


            print("Doc Name:", doctor, "Time in:", time_in, "Time out:", time_out)
            
            print("Daily Reporting:", daily_reporting)
            
            # Convert time strings to datetime.time objects
            time_in = datetime.strptime(time_in, "%H:%M").time()
            time_out = datetime.strptime(time_out, "%H:%M").time()
            if time_in > time_out:
                print("Time in greater than time out")
                messages.error(request,"Please provide correct time in and time out information.")
            elif time_in == time_out:
                print("Time in equal to time out")
                messages.error(request,"Time in and Time out must be different.")
            else:
                
                data = DoctorAdded(
                    daily_reporting=daily_reporting,
                    doctor=doctor,
                    doctor_time_in=time_in,
                    doctor_time_out=time_out,
                    status = True
                )
                data.save()
            return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
    
        if 'product' in request.POST and 'product_unit' in request.POST and 'product_qty' in request.POST:
            product_id = request.POST.get('product')
            unit_id = request.POST.get('product_unit')
            quantity = request.POST.get('product_qty')
            doctor_id = request.session.get('selected_doctor_id',None)

            product = ProductMaster.objects.get(id=int(product_id))
            unit = UnitMaster.objects.get(id=int(unit_id))
            doctor = DoctorMaster.objects.get(id=int(doctor_id))
            
            print("Product: ", product, "Unit: ", unit, "Qty: ", quantity, "DocId:", doctor)
            print("Daily Reporting:", daily_reporting)

            data = ProductAdded(
                product=product,
                unit=unit,
                quantity=quantity,
                doctor=doctor,
                daily_reporting=daily_reporting
            )
            data.save()
            return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
        
        if 'gift' in request.POST and 'gift_unit' in request.POST and 'gift_qty' in request.POST:
            gift_id = request.POST.get('gift')
            unit_id = request.POST.get('gift_unit')
            quantity = request.POST.get('gift_qty')
            doctor_id = request.session.get('selected_doctor_id',None)

            gift = GiftMaster.objects.get(id=int(gift_id))
            unit = UnitMaster.objects.get(id=int(unit_id))
            doctor = DoctorMaster.objects.get(id=int(doctor_id))

            print("Gift:", gift, "Unit:", unit, "Quantity:",quantity)

            data = GiftAdded(
                gift=gift,
                unit=unit,
                quantity=quantity,
                doctor=doctor,
                daily_reporting=daily_reporting
            )
            data.save()
            return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
        
        if 'stockist' in request.POST and 'stockist_arrival_time' in request.POST and 'stockist_departure_time' in request.POST:
            stockist_id = request.POST.get('stockist')
            time_in = request.POST.get('stockist_arrival_time')
            time_out = request.POST.get('stockist_departure_time')
            doctor_id = request.session.get('selected_doctor_id')
            stockist = StockistMaster.objects.get(id=int(stockist_id))

            print("Stockist:", stockist, "Time in:", time_in, "Time out:", time_out)
            
            
            # Convert time strings to datetime.time objects
            time_in = datetime.strptime(time_in, "%H:%M").time()
            time_out = datetime.strptime(time_out, "%H:%M").time()
            if time_in > time_out:
                print("Time in greater than time out")
                messages.error(request,"Please provide correct time in and time out information.")
            elif time_in == time_out:
                print("Time in equal to time out")
                messages.error(request,"Time in and Time out must be different.")
            else:
                data = StockistAdded(
                    stockist=stockist,
                    stockist_time_in=time_in,
                    stockist_time_out=time_out,
                    daily_reporting=daily_reporting,
                )
                data.save()
            return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
        
        if 'doctor_update' in request.POST:
            print("hello 2")
            doctor_update_id = request.POST.get('doctor_update')
            print("Doctor_id:", doctor_update_id)
            doctor_update = DoctorAdded.objects.filter(daily_reporting_id=daily_reporting_id).get(pk=doctor_update_id)
            print("Doctor_update:", doctor_update)
            return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
        
    
    doctors_added = None
    products_added = None
    gifts_added = None
    stockist_added = None

    daily_reporting_id = DailyReporting.objects.filter(employee_id=id).filter(date_of_working=date).get()
    doctors_added = DoctorAdded.objects.filter(daily_reporting_id=daily_reporting_id)
    print(doctors_added)


    products_added = ProductAdded.objects.filter(daily_reporting_id=daily_reporting_id).filter(doctor_id=doctor_id)
    print(products_added)


    gifts_added = GiftAdded.objects.filter(daily_reporting_id=daily_reporting_id).filter(doctor_id=doctor_id)
    print(gifts_added)

    
    stockist_added = StockistAdded.objects.filter(daily_reporting_id=daily_reporting_id)
    print(stockist_added)


    doctorAdded = False
    productAdded = False
    giftAdded = False
    stockistAdded = False
    if DoctorAdded.objects.filter(daily_reporting_id=daily_reporting_id).exists():
        doctorAdded = True

    if ProductAdded.objects.filter(daily_reporting_id=daily_reporting_id).exists():
        productAdded = True

    if GiftAdded.objects.filter(daily_reporting_id=daily_reporting_id).exists():
        giftAdded = True

    if StockistAdded.objects.filter(daily_reporting_id=daily_reporting_id).exists():
        stockistAdded = True
    
    if doctorAdded and productAdded and giftAdded and stockistAdded:
        showSubmitWarning = False

    context = {
        'employee': employee,
        'employee_id': employee_id,
        'tour_id': tour_id,
        'designation': designation,
        'tour_program': tour_program,
        'date': date,
        'source_area': from_area,
        'destination_area': to_area,
        'doctors': doctors,
        'stockists': stockists,
        'products': products,
        'gifts': gifts,
        'units': units,
        'doctors_added': doctors_added,
        'products_added': products_added,
        'gifts_added': gifts_added,
        'stockists_added': stockist_added,
        'showSubmitWarning': showSubmitWarning
    }
    return render(request, 'daily_report_form_detail.html', context)


def update_doctor(request, id, tour_id, doc_id):
    if request.method == 'POST':
        tour_program = TourProgram.objects.get(id=tour_id)
        date = tour_program.date_of_tour
        daily_reporting_id = DailyReporting.objects.filter(employee_id=id).filter(date_of_working=date).get().id
        print("Daily reporting id:", daily_reporting_id)
        doctor_update = DoctorAdded.objects.filter(daily_reporting_id=daily_reporting_id).get(doctor_id=doc_id)
        # doctor_update_id = doctor_update.id
        doctor = request.POST.get('doctor')
        time_in = request.POST.get('doctor_arrival_time')
        time_out = request.POST.get('doctor_departure_time')

        doctor = DoctorMaster.objects.get(id=int(doctor))

        print("Doctor:", doctor, "Time in:", time_in, "Time out:", time_out)

        print("Doctor Update:", doctor_update)

        # Convert time strings to datetime.time objects
        time_in = datetime.strptime(time_in, "%H:%M").time()
        time_out = datetime.strptime(time_out, "%H:%M").time()
        if time_in > time_out:
            print("Time in greater than time out")
            messages.error(request,"Please provide correct time in and time out information.")
        elif time_in == time_out:
            print("Time in equal to time out")
            messages.error(request,"Time in and Time out must be different.")
        else:
            doctor_update.doctor = doctor
            doctor_update.doctor_time_in = time_in
            doctor_update.doctor_time_out = time_out
            doctor_update.save()
            pass

        return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
    
def update_product(request, id, tour_id, product_id):
    if request.method == 'POST':
        tour_program = TourProgram.objects.get(id=tour_id)
        date = tour_program.date_of_tour
        daily_reporting_id = DailyReporting.objects.filter(employee_id=id).filter(date_of_working=date).get().id
        print("Daily reporting id:", daily_reporting_id)
        product_update = ProductAdded.objects.filter(daily_reporting_id=daily_reporting_id).get(product_id=product_id)
        
        product = request.POST.get('product')
        product_unit = request.POST.get('product_unit')
        product_qty = request.POST.get('product_qty')

        product = ProductMaster.objects.get(id=int(product))
        product_unit = UnitMaster.objects.get(id=int(product_unit))

        print("Product:", product, "Unit:", product_unit, "Quantity:", product_qty)

        print("Product Update:", product_update)

        product_update.product = product
        product_update.unit = product_unit
        product_update.quantity = product_qty
        product_update.save()

        return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
    

def update_gift(request, id, tour_id, gift_id):
    if request.method == 'POST':
        tour_program = TourProgram.objects.get(id=tour_id)
        date = tour_program.date_of_tour
        daily_reporting_id = DailyReporting.objects.filter(employee_id=id).filter(date_of_working=date).get().id
        print("Daily reporting id:", daily_reporting_id)
        gift_update = GiftAdded.objects.filter(daily_reporting_id=daily_reporting_id).get(gift_id=gift_id)
        
        gift = request.POST.get('gift')
        gift_unit = request.POST.get('gift_unit')
        gift_qty = request.POST.get('gift_qty')

        gift = GiftMaster.objects.get(id=int(gift))
        gift_unit = UnitMaster.objects.get(id=int(gift_unit))

        print("Gift:", gift, "Unit:", gift_unit, "Quantity:", gift_qty)

        print("Gift Update:", gift_update)

        gift_update.gift = gift
        gift_update.unit = gift_unit
        gift_update.quantity = gift_qty
        gift_update.save()

        return redirect('daily_report_form_detail', id=id, tour_id=tour_id)
    

def update_stockist(request, id, tour_id, stockist_id):
    if request.method == 'POST':
        tour_program = TourProgram.objects.get(id=tour_id)
        date = tour_program.date_of_tour
        daily_reporting_id = DailyReporting.objects.filter(employee_id=id).filter(date_of_working=date).get().id
        print("Daily reporting id:", daily_reporting_id)
        stockist_update = StockistAdded.objects.filter(daily_reporting_id=daily_reporting_id).get(stockist_id=stockist_id)
        
        stockist = request.POST.get('stockist')
        time_in = request.POST.get('stockist_arrival_time')
        time_out = request.POST.get('stockist_departure_time')

        stockist = StockistMaster.objects.get(id=int(stockist))

        print("Stockist:", stockist, "Time in:", time_in, "Time out:", time_out)

        print("Stockist Update:", stockist_update)

        # Convert time strings to datetime.time objects
        time_in = datetime.strptime(time_in, "%H:%M").time()
        time_out = datetime.strptime(time_out, "%H:%M").time()
        if time_in > time_out:
            print("Time in greater than time out")
            messages.error(request,"Please provide correct time in and time out information.")
        elif time_in == time_out:
            print("Time in equal to time out")
            messages.error(request,"Time in and Time out must be different.")
        else:
            stockist_update.stockist = stockist
            stockist_update.stockist_time_in = time_in
            stockist_update.stockist_time_out = time_out
            stockist_update.save()

        return redirect('daily_report_form_detail', id=id, tour_id=tour_id)

        
def daily_report_form_detail_delete_doctor(request, id, tour_id, pk):
    if request.method == 'POST':
        doctor = DoctorAdded.objects.get(pk=pk)
        print(doctor)
        doctor.delete()
        return HttpResponseRedirect(reverse('daily_report_form_detail', kwargs={'id': id, 'tour_id': tour_id}))
    

def daily_report_form_detail_delete_product(request, id, tour_id, pk):
    if request.method == 'POST':
        product = ProductAdded.objects.get(pk=pk)
        print(product)
        product.delete()
        return HttpResponseRedirect(reverse('daily_report_form_detail', kwargs={'id': id, 'tour_id': tour_id}))
    
def daily_report_form_detail_delete_gift(request, id, tour_id, pk):
    if request.method == 'POST':
        gift = GiftAdded.objects.get(pk=pk)
        print(gift)
        gift.delete()
        return HttpResponseRedirect(reverse('daily_report_form_detail', kwargs={'id': id, 'tour_id': tour_id}))
    

def daily_report_form_detail_delete_stockist(request, id, tour_id, pk):
    if request.method == 'POST':
        stockist = StockistAdded.objects.get(pk=pk)
        print(stockist)
        stockist.delete()
        return HttpResponseRedirect(reverse('daily_report_form_detail', kwargs={'id': id, 'tour_id': tour_id}))


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