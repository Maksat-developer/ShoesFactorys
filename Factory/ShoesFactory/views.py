from django.shortcuts import render
from .models import ProductSale



def index(request):
    product = ProductSale.objects.all()
    context = {
        "product": product

    }
    return render(request, "ShoesFactory/index.html", context=context)