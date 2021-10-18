from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Order form to be compeleted by user on checkout """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',
                  'country')
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classses and remove labels
        """

        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'John Smith',
            'email': 'john@smith.com',
            'phone_number': 'Phone Number',
            'street_address1': 'Address Line 1',
            'street_address2': 'Address Line 2',
            'town_or_city': 'Town or City',
            'postcode': 'Post Code',
            'county': 'County',
            'country': 'Country'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attr['placeholder'] = placeholders
            self.fields[field].label = False
