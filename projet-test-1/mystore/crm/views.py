from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customer':customers, 'total_orders':total_orders,
               'delivered':delivered, 'pending':pending}

    return render(request, 'crm/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'crm/products.html', {'products':products})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customers.html', {'customer':customers})

def orders(request):
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'total_orders':total_orders,
               'delivered':delivered, 'pending':pending}
    
    return render(request, 'crm/orders.html', context)