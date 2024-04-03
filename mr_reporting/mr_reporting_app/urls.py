from django.urls import path
from mr_reporting_app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('form/', views.daily_report_form, name='daily_report_form'),
    path('admin/mr_reporting_app/areamaster/add/', views.areamaster_add, name='areamaster_add')
]