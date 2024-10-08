from django.contrib import admin
from catalog_2.models import Product


# Register your models here.


@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "created_at", "view_counter", "number_version", "name_version")
    list_filter = ("is_active", "name", "created_at", "view_counter")
    search_fields = ("name", "number_version", "name_version")
