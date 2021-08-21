from django.contrib import admin
from .models import City, Shipment
from rangefilter.filters import DateRangeFilter

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "state"]
    list_display_links = ["name", "state"]
    search_fields = ["name", "state"]


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ["id", "date_shipment", "date_received", "order", "city"]
    list_display_links = ["date_shipment", "date_received"]
    list_filter = [("date_shipment", DateRangeFilter)]
    search_fields = ["date_shipment", "date_received"]
    raw_id_fields = ["order", "city"]
