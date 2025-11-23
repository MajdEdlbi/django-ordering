from django.contrib import admin
from .models import Item
admin.site.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")