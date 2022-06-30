from cProfile import label
from unicodedata import category
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from .models import Category, Customer, OrderDetail, Product, Vendor,UserType, Shop, Order
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

def index(request):
    return render(request,'html/index.html')


def vendor(request,id):
    vendor=Vendor.objects.get(pk=id)

    return render(request,"html/vendor.html",{"vendor":vendor})

def updateVendor(request,id):
    if request.method=="POST":
        value=VendorForm(request.POST)
        if value.is_valid():
            new_name=value.cleaned_data["vendor_name"]
            new_number=value.cleaned_data["vendor_number"]
            new_email=value.cleaned_data["vendor_email"]
            new_password=value.cleaned_data["vendor_password"]
     
            vendor=Vendor.objects.get(pk=id)
            
            vendor.name=new_name
            vendor.number=new_number
            vendor.password=new_password
            vendor.email=new_email
            vendor.save()
            return HttpResponseRedirect(reverse("main:vendor-profile", args=[id]))
    return render(request,"html/updateVendor.html",{"form":VendorForm()})
 
    
def displayVendor(request):
    lists=Vendor.objects.all()
    return render(request, "html/list.html",{"list":lists})

def product(request):
    products=Product.objects.all()
    return render(request,"html/product.html",{"products":products})

# def layout(request):
#     return render(request, 'html/layout.html')
FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class AddProduct(forms.Form):
    name=forms.CharField(max_length=50)
    description=forms.CharField(max_length=100)
    shop=forms.MultipleChoiceField(
        initial='0',
        required=True,
        widget=forms.SelectMultiple(),
        choices=[(shop.id , shop.name) for shop in Shop.objects.all()]
        
    )
    category=forms.CharField(
        required=False,
        widget=forms.Select(choices=[(category.id, category.name) for category in Category.objects.all()])
        
    )
def addProduct(request):
    if request.method=="POST":
        value=AddProduct(request.POST)
        if value.is_valid():
            new_name=value.cleaned_data["name"]
            new_description=value.cleaned_data["description"]
            new_shop=value.cleaned_data["shop"]
            new_category=value.cleaned_data["category"]
            
            
            product = Product.objects.create(
                name=new_name,
                description=new_description,
                category_id=new_category
            )
            qs=list(Shop.objects.filter(id__in=new_shop))

            product.shop.add(*qs)
            return HttpResponseRedirect(reverse("main:product"))
 
    return render(request,"html/addProduct.html",{"form":AddProduct()})


def deleteProduct(request, id):
    Product.objects.get(pk=id).delete()
    
    return HttpResponseRedirect(reverse('main:product'))

def updateProduct(request, id):
    if request.method=="POST":
        value=AddProduct(request.POST)
        if value.is_valid():
            new_name=value.cleaned_data["name"]
            new_description=value.cleaned_data["description"]
            new_shop=value.cleaned_data["shop"]
            new_category=value.cleaned_data["category"]
            
            qs=list(Shop.objects.filter(id__in=new_shop))

           
            
            product=Product.objects.get(pk=id)
          
            product.name=new_name
            product.description=new_description
            product.shop.add(*qs)
            product.category_id=int(new_category)
            product.save()
            return HttpResponseRedirect(reverse("main:product"))
 

    return render(request,"html/updateProduct.html",{"form":AddProduct()})

def order(request):
    orders=Order.objects.all()
    return render(request,'html/orderlist.html',{"orders":orders})

def orderDetail(request,id):
    order=Order.objects.get(pk=id)
    return render(request,'html/orderDetail.html',{"order":order})

def productDetail(request,id):
    product=Product.objects.get(pk=id)
    return render(request,'html/productDetail.html',{"product":product})

def shop(request,id):
    shops=Shop.objects.get(pk=id)
    products=Shop.objects.filter(product__pk=id)
    return render(request,'html/shoplist.html',{"shops":shops, "products":products})


# def updateProduct(request):
#     if request.method=="POST":
#         value=AddProduct(request.POST)
#         if value.is_valid():
#             new_name=value.cleaned_data["name"]
#             new_description=value.cleaned_data["description"]
#             new_shop=value.cleaned_data["shop"]
#             new_category=value.cleaned_data["category"]
            
            
#             product = Product.objects.create(
#                 name=new_name,
#                 description=new_description,
#                 category_id=new_category
#             )
#             qs=list(Shop.objects.filter(id__in=new_shop))

#             product.shop.add(*qs)
#             return HttpResponseRedirect(reverse("main:product"))
 
#     return render(request,"html/updateProduct.html",{"form":AddProduct()})

