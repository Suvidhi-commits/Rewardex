from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.merchant_dashboard, name="merchantDashboard"),
    path('merchant/login/', views.merchant_login, name="merchantLogin"),
    path('merchant/events/', views.merchant_events, name="merchantEvents"),
    path('merchant/welcome/', views.merchant_welcome, name="merchantWelcome"),
    path('merchant/scratch/form/', views.scratch_event, name="merchantScratch"),
]