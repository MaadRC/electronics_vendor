
from django.contrib import admin
from .models import Product, Customer, Order, OrderItem

from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_contract_customer', 'account_number')
    list_filter = ('is_contract_customer',)
    search_fields = ('name', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date', 'total_amount', 'status')
    list_filter = ('status', 'date')
    search_fields = ('customer__name', 'status')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_filter = ('product',)
    search_fields = ('product__name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)



