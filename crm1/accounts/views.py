from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)

def customer(request):
    template_name = 'accounts/customer.html'
    return render(request, template_name)

def products(request):
    template_name = 'accounts/products.html'
    return render(request, template_name)

