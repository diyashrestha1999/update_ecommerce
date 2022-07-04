from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('vendorprofile/<int:id>',views.vendor,name="vendor-profile"),
    path('vendorlist/',views.displayVendor,name="displayVendor"),
    path('updatevendor/<int:id>',views.updateVendor,name="update-vendor"),
    path('deletevendor/<int:id>',views.deleteVendor,name="delete-vendor"),
    path('addvendor/',views.addVendor,name="add-vendor"),
    # path('layout/',views.layout, name="layout"),
    path('product/',views.product,name="product"),
    path('addproduct/',views.addProduct,name="add-product"),
    path('deleteproduct/<int:id>',views.deleteProduct,name="delete-product"),
    path('updateproduct/<int:id>',views.updateProduct,name="update-product"),
    path('orderlist/',views.order,name="order"),
    path('orderdetail/<int:id>',views.orderDetail,name="order-detail"),
    path('productdetail/<int:id>',views.productDetail,name="product-detail"),
    path('shop/<int:id>',views.shop,name="shop"),
    path('shoplist/',views.shoplist,name="shoplist"),
    path('category/',views.caregoryList,name="category"),
    path('categorydetail/<int:id>',views.caregoryDetail,name="category-detail"),
    path('customerprofile/<int:id>',views.customer,name="customer-profile"),
    path('customerlist/',views.displayCustomer,name="displayCustomer"),
    path('addcustomer/',views.addCustomer,name="add-customer"),
    path('updatcustomer/<int:id>',views.updateCustomer,name="update-customer"),
    path('deletecustomer/<int:id>',views.deleteCustomer,name="delete-customer"),
    path('addshop/',views.addShop,name="add-shop"),
    path('updateshop/<int:id>',views.updateShop,name="update-shop"),
    path('deleteshop/<int:id>',views.deleteShop,name="delete-shop"),
    path('deletecategory/<int:id>',views.deleteCategory,name="delete-category"),
    path('dashboard-view/',views.viewDashboard,name="viewDashboard"),
    path('',views.product,name="index") 
]
