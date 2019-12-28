from . import views
from django.urls import path

app_name = "products"

urlpatterns = [
     path('products/',views.Products,name="products") ,
     path('products2/<args>/',views.Products,name="products2") ,
     path('products_form/',views.products_form,name="products_form"),
     path('product_detail/<slug>/',views.product_detail,name="product_detail"),
     path('Editproduct/<slug>/',views.Editproduct,name="Editproduct"),
     path('removeitem/<int:id>/',views.removeitem,name="removeitem")
]
