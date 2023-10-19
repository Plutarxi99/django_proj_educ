from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):
    def clean(self):
        exclude_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        data = self.cleaned_data
        for word in exclude_word:
            if word in data['name']:
                raise ValidationError('Запрещенные слова не допускаются')
        return data

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'category', 'price',)
        # exclude = ('',)
