from django import forms

from catalog_2.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # exclude = ("photo",)
        # fields = '__all__'
        fields = ('name', 'number_version', 'name_version', 'photo', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        list_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in list_words:
            if i in cleaned_data:
                raise forms.ValidationError('В названии недопустимое слово')
        return cleaned_data