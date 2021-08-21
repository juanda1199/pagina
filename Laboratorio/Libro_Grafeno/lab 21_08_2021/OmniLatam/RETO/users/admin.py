from django.contrib import admin
from .models import User, Notification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ["document", "name", "phone", "type", ]
    list_display_links = ["document", "name" ]
    search_fields = ["name", ]


@admin.register(Notification)
class NotificationDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "tittle", "resume", "user"]
    list_display_links = ["tittle", ]
    search_fields = ["id", "tittle", ]
    raw_id_fields = ["user", ]
