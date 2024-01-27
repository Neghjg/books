from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "price", "quantity"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user' ,'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    readonly_fields = ('user' ,'first_name', 'last_name', 'email',)
    search_fields = ['id', ]
    inlines = [OrderItemInline]
    
    
class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = ["requires_delivery", "payment_on_get", "paid"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)