from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from catalog_2.forms import ProductForm
from catalog_2.models import Product


# Create your views here.


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ("name", "number_version", "name_version", "photo", "is_active")
    success_url = reverse_lazy("catalog_2:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ("name", "number_version", "name_version", "photo", "is_active")
    success_url = reverse_lazy("catalog_2:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog_2:product_list")


def contacts(request):
    return render(request, "catalog_2/contacts.html")