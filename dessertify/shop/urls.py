from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('gallery/', views.gallery, name="gallery"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),

]
