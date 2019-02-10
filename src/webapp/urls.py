from django.contrib import admin
from django.urls import path,include
from webapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('shop',views.shop,name="shop"),
    path('about',views.about,name="about"),
    path('product/<product_name>/<pk>',views.products_detail,name="product_detail"),
    path('category/<category_name>/<pk>',views.category,name="category"),
    path('feature',views.feature,name="feature"),
    path('contact',views.contact,name="contact"),


]
