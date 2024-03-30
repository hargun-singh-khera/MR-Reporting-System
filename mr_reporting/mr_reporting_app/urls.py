from django.urls import path
from mr_reporting_app import views

urlpatterns = [
    path('', views.index, name='index')
]