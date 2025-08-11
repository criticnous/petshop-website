from django.urls import path
from . import views

urlpatterns = [
    # This is the root URL for your site (the homepage)
    path('', views.home, name='home'), 
    path('pets/', views.pet_list, name='pet-list'),
    path('products/', views.product_list, name='product-list'),
]
