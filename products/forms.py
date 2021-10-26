from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """ Form for addming a product """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class ReviewForm(forms.ModelForm):
    """ Form for adding a product review """

    class Meta:
        model = Review
        fields = ('body', 'recommend')

    def __init__(self, *args, **kwargs):
        """ Override placeholder """

        super().__init__(*args, **kwargs)
        self.fields['body'].label = False
        self.fields['body'].widget.attrs['rows'] = 3
        self.fields['body'].widget.attrs['placeholder'] = 'What do you think?'
        self.fields['recommend'].label = 'Would you recommend it?'
