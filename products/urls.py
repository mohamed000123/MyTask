from django.urls import path
from .views import product_create, get_user_products, get_all_products, get_specific_products

urlpatterns = [

    path('productCreate', product_create.as_view()),
    path('myProducts', get_user_products.as_view()),
    path('AllProducts', get_all_products.as_view()),
    path('searchProducts', get_specific_products.as_view()),

]
