from django.core.exceptions import ValidationError
from django.db import models

from catalog.models import Product, Version
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, Fieldset
from crispy_forms.bootstrap import FormActions, ContainerHolder


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


class VersionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        # self.helper.layout = Layout(
        #     Fieldset(
        #         'Версия продукта',
        #         'product_name',
        #         'version_number',
        #         'version_name',
        #         'version_is'
        #     ),
        #     FormActions(
        #         Submit('save', 'Save changes', css_class='btn-success mt-4'),
        #         Button('cancel', 'Cancel', css_class='btn-warning mt-4 pl-4', ),
        #     ),
        #
        # )

        self.helper.layout = Layout(
            ContainerHolder(
                'product_name',
                'version_number',
                'version_name',
                'version_is_active',
                css_id='text-center',
                css_class='p-3 bg-secondary bg-gradient text-white'
            ),
            FormActions(
                Submit('save', 'Save changes', css_class='btn-success mt-4', css_id=''),
                Button('cancel', 'Cancel', css_class='btn-warning mt-4 pl-4', onclick="window.history.back()"),
            )
        )

    class Meta:
        model = Version
        fields = '__all__'
        # fields = ('product_name', 'version_number', 'version_name', 'version_is_active',)
        # exclude = ('',)


class VersionFormProduct(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'