from django.shortcuts import render
from .models import Pet, Product

def home(request):
    # Get the 3 most recently added pets and products to feature on the homepage
    featured_pets = Pet.objects.filter(is_available=True).order_by('-date_added')[:3]
    featured_products = Product.objects.filter(is_available=True).order_by('?')[:3] # '?' orders randomly
    
    context = {
        'pets': featured_pets,
        'products': featured_products,
    }
    return render(request, 'store/home.html', context)

def pet_list(request):
    all_pets = Pet.objects.filter(is_available=True)
    context = {
        'pets': all_pets,
    }
    return render(request, 'store/pet_list.html', context)

def product_list(request):
    all_products = Product.objects.filter(is_available=True)
    context = {
        'products': all_products,
    }
    return render(request, 'store/product_list.html', context)
