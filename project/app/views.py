from django.shortcuts import render
from django.db.models import Q, F
from .models import Product

Q1 = Product.objects.filter(Q(price__gt=50) | Q(quantity__lt=10))
Q2 = Product.objects.filter(Q(name__icontains="phone") &Q(price__range=(100, 500)))
Q3 = Product.objects.filter(~Q(price__lt=200))

F1 = Product.objects.update(price=F("price") + 10)
F2 = Product.objects.filter(price__gt=F("quantity"))
F3 = Product.objects.update(quantity=F("quantity") + 1)