from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Electronics Vendor Homepage!")

def product_list(request):
    products = Product.objects.all()
    print(products)  
    return render(request, 'webapp/product_list.html', {'products': products})
