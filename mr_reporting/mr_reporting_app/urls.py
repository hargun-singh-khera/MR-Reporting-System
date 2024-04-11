from django.urls import path
from mr_reporting_app import views

urlpatterns = [
    path('', views.redirect_url, name='redirect_url'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('form/', views.daily_report_form, name='daily_report_form'),
    path('report/', views.report, name='report')
]