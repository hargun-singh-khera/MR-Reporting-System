from django.urls import path
from mr_reporting_app import views

urlpatterns = [
    path('', views.redirect_url, name='redirect_url'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('form/', views.daily_report_form, name='daily_report_form'),
    path('form/submit/<int:tour_id>', views.submit_form, name='submit_form'),
    path('form/<int:id>/<int:tour_id>', views.daily_report_form_tour, name='daily_report_form_tour'),
    path('form/employee/<int:id>/tourprogram/<int:tour_id>', views.daily_report_form_detail, name='daily_report_form_detail'),
    path('form/employee/<int:id>/tourprogram/<int:tour_id>/doctor/delete/<int:pk>', views.daily_report_form_detail_delete_doctor, name='daily_report_form_detail_delete_doctor'),
    path('form/employee/<int:id>/tourprogram/<int:tour_id>/product/delete/<int:pk>', views.daily_report_form_detail_delete_product, name='daily_report_form_detail_delete_product'),
    path('form/employee/<int:id>/tourprogram/<int:tour_id>/gift/delete/<int:pk>', views.daily_report_form_detail_delete_gift, name='daily_report_form_detail_delete_gift'),
    path('form/employee/<int:id>/tourprogram/<int:tour_id>/stockist/delete/<int:pk>', views.daily_report_form_detail_delete_stockist, name='daily_report_form_detail_delete_stockist'),
    
    path('report/', views.report, name='report'),
]