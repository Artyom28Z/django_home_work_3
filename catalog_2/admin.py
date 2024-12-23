from django.contrib import admin
from catalog_2.models import Product, Version, Category


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "view_counter", "is_active")
    list_filter = ("name", "created_at", "view_counter")
    search_fields = ("name",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "number_version", "is_active", "name_version")
    list_filter = ("number_version", "name_version", "is_active")
    search_fields = ("product", "number_version", "name_version", "is_active")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
