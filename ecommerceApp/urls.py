from django.urls import path
from . import views

app_name="main"
urlpatterns = [
    path('',views.index,name="index"),
    path('vendorprofile/<int:id>',views.vendor,name="vendor-profile"),
    path('vendorlist/',views.displayVendor,name="displayVendor"),
    path('updatevendor/<int:id>',views.updateVendor,name="update-vendor"),
    # path('layout/',views.layout, name="layout"),
    path('product/',views.product,name="product"),
    path('addproduct/',views.addProduct,name="add-product"),
    path('deleteproduct/<int:id>',views.deleteProduct,name="delete-product"),
    path('updateproduct/<int:id>',views.updateProduct,name="update-product"),
    path('orderlist/',views.order,name="order"),
    path('orderdetail/<int:id>',views.orderDetail,name="order-detail"),
    path('productdetail/<int:id>',views.productDetail,name="product-detail"),
    path('shop/<int:id>',views.shop,name="shop"),
    # path('updateproduct/',views.updateProduct, name="updateproduct")
   
    
]
