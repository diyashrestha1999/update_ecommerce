from cProfile import label
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import Customer, Vendor,UserType
# Create your views here.
class VendorForm(forms.Form):
    vendor_name=forms.CharField(label='Vendor Name:',max_length=50)
    vendor_number=forms.IntegerField(label='Vendor Number')
    vendor_email=forms.EmailField(label="Email")
    vendor_password = forms.CharField(label="Password",widget=forms.PasswordInput)    


class CustomerForm(forms.Form):
    customer_name=forms.CharField(label="Name:", max_length=50)
    customer_username=forms.CharField(label="Username:", max_length=50)
    customer_email=forms.EmailField(label="Email")
    customer_password = forms.CharField(label="Password",widget=forms.PasswordInput)    


def vendor(request):
    if request.method=="POST":
        values=VendorForm(request.POST)
        if values.is_valid():
            clean_name=values.cleaned_data["vendor_name"]
            clean_number=values.cleaned_data["vendor_number"]
            clean_email=values.cleaned_data["vendor_email"]
            clean_password=values.cleaned_data["vendor_password"]


            Vendor.objects.create(
            name=clean_name,number=clean_number, email=clean_email, password=clean_password)
            
            return HttpResponseRedirect(reverse("main:displayVendor"))

    return render(request,"html/index.html",{"vendorform":VendorForm(), "customerform":CustomerForm()})

def customer(request):
    if request.method=="POST":
        values=CustomerForm(request.POST)
        if values.is_valid():
            new_name=values.cleaned_data["customer_name"]
            new_username=values.cleaned_data["customer_name"]
            new_email=values.cleaned_data["customer_email"]
            new_password=values.cleaned_data["customer_password"]

            Customer.objects.create(name=new_name,username=new_username,email=new_email,password=new_password)
            return HttpResponseRedirect(reverse("main:displayCustomer"))
    
    return render(request,'html/includes/customerForm.html',{"form":CustomerForm()})


def displayVendor(request):
    lists=Vendor.objects.all()
    return render(request, "html/list.html",{"list":lists})

# def layout(request):
#     return render(request, 'html/layout.html')
