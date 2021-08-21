from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["name", "stock", ]
    list_display_links = ["name", ]
    search_fields = ["name", ]
