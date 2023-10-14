from django.shortcuts import render

from .models import *

def home(request):
    return render(request, 'crm/intro.html')

def products(request):
    products = Product.objects.all()

    total_products = products.count()

    actif = products.filter(status='True').count()
    inactif = products.filter(status='False').count()

    context = {'products':products, 'total_products':total_products, 'actif':actif,
               'inactif':inactif}

    return render(request, 'crm/products.html', context)

def customers(request):
    customers = Customer.objects.all()
    
    total_customers = customers.count()

    actif = customers.filter(status='True').count()
    inactif = customers.filter(status='False').count()

    context = {'customer':customers, 'total_customers':total_customers, 'actif':actif,
               'inactif':inactif}

    return render(request, 'crm/customers.html', context)

def orders(request):
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Livrée').count()
    pending = orders.filter(status='En attente').count()

    context = {'orders':orders, 'total_orders':total_orders,
               'delivered':delivered, 'pending':pending}
    
    return render(request, 'crm/orders.html', context)