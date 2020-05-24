from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'shop/main.html')


def shop(request):
    context = {}
    return render(request, 'shop/shop.html', context)


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)


def gallery(request):
    context = {}
    return render(request, 'shop/gallery.html', context)


def contact(request):
    context = {}
    return render(request, 'shop/contact.html', context)