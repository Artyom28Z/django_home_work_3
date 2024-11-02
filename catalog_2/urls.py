from django.urls import path
from django.views.decorators.cache import cache_page

from catalog_2.apps import Catalog2Config
from catalog_2.views import (
    contacts,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryCreateView,
    CategoryListView,
)

app_name = Catalog2Config.name


urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("create_product/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("create_category/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("contacts/", contacts, name="contacts"),
]
