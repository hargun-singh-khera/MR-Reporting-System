from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
    else:
        return render(request, 'login.html')

def daily_report_form(request):
    return render(request, 'detail_report_form.html')

def areamaster_add(request):
    return HttpResponse("Area Master")
