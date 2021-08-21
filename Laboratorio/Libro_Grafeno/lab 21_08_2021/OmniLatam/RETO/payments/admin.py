from django.contrib import admin
from .models import Payment, PaymentOrder


class PaymentInline(admin.TabularInline):
    model = PaymentOrder
    extra = 1


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]
    list_display = ["payment_type", "payment_total", ]
    list_display_links = ["payment_total", ]
    search_fields = ["id", "payment_total", ]


@admin.register(PaymentOrder)
class PaymentOrderAdmin(admin.ModelAdmin):
    list_display = ["total_payment_order", "subtotal", "order", "payment"]
    list_display_links = ["payment", "order", ]
    search_fields = ["id", "order", ]
    raw_id_fields = ["payment", "order", ]


