from django.contrib import admin

from .models import *


class ProductSaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'articul', 'price', 'package', 'status']
    list_filter = ['articul', 'type_pr', 'size']


admin.site.register(ProductSale, ProductSaleAdmin)

admin.site.register(StatusProduct)
admin.site.register(ProductModel)
admin.site.register(Employee)
admin.site.register(CounterpartiesRegion)
admin.site.register(Counterparties)
admin.site.register(Balance)
admin.site.register(DebtOn)
admin.site.register(ZPeople)
