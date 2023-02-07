from django.shortcuts import render

# Create your views here.\

def home(request):
    return render(request, 'customer/home.html')

def cart(request):
    return render(request, 'customer/cart.html')

def change_passwd(request):
    return render(request, 'customer/chge pswd.html')

def my_orders(request):
    return render(request, 'customer/myorders.html')

def product_details(request):
    return render(request, 'customer/product details.html')

def profile(request):
    return render(request, 'customer/profile.html')