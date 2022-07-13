from django.shortcuts import render
from .models import ProductSale, Employee


def index(request):
    product = ProductSale.objects.all()
    context = {
        "product": product

    }
    return render(request, "ShoesFactory/index.html", context=context)


def community(request):
    commuinty = Employee.objects.all()
    context = {
        "commuinty": commuinty
    }
    return render(request, template_name="ShoesFactory/commuinty.html", context=context)