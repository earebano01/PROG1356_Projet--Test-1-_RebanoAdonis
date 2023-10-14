from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.products, name='product'),
    path('customer/', views.customers, name='customer'),
    path('orders/', views.orders, name='orders'),
]
