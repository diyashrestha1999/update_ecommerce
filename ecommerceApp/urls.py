from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('',views.vendor,name="vendor"),
    path('vendorlist/',views.displayVendor,name="displayVendor"),
    path('customer/',views.customer, name="customer"),
    # path('layout/',views.layout, name="layout"),
   
    
]
