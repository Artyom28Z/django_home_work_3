from django import forms
from django.forms import BooleanField

from catalog_2.models import Product, Category


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (
            field_name,
            field,
        ) in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-class"


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category", "is_active")


class CategoryForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("view_counter", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]
        list_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for i in list_words:
            if i in cleaned_data:
                raise forms.ValidationError("В названии недопустимое слово")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        list_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for i in list_words:
            if i in cleaned_data:
                raise forms.ValidationError("В описании недопустимое слово")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
