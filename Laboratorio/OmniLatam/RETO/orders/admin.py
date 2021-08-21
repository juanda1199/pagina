from django.contrib import admin
from .models import Order, OrderDetail
from rangefilter.filters import DateRangeFilter


class OrderInline(admin.TabularInline):
    model = OrderDetail
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    list_display = ["id", "user", "date_order", "order_total"]
    list_display_links = ["user", ]
    search_fields = ["name", "barcode", "id"]


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "order",  "price", "quantity", "subtotal"]
    list_display_links = ["id", "product", "order", ]
    list_filter = [("date_order", DateRangeFilter)]
    search_fields = ["id", "order", ]
    raw_id_fields = ["product", "order", ]
