from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'crm/dashboard.html')

def products(request):
    return render(request, 'crm/products.html')

def customers(request):
    return render(request, 'crm/customers.html')