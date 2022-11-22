from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Products

# Create your views here.

# ГЛАВНАЯ
def index(request):
    return render(request, 'home.html')

# ПРОФИЛЬ
def profile(request):
    return render(request, 'profile.html')

def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})

def create(request):
    if request.method == "POST":
        product = Products()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.save()
    return HttpResponseRedirect("/products")