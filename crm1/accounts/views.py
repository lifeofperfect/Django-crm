from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered_orders = orders.filter(status='Delivered').count()
    pending_orders = orders.filter(status='Pending').count()

    template_name = 'accounts/dashboard.html'
    context = {
        'orders':orders,
        'customers':customers,
        'total_orders':total_orders,
        'delivered':delivered_orders,
        'pending':pending_orders
    }
        
    return render(request, template_name, context)

def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    template_name = 'accounts/customer.html'
    context = {
        'customers':customers,
        'orders':orders,

    }
    return render(request, template_name, context)

def products(request):
    products = Product.objects.all()
    template_name = 'accounts/products.html'
    context = {
        'products':products
    }
    return render(request, template_name, context)

