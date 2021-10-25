from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Order form to be compeleted by user on profile """
    class Meta:
        model = UserProfile
        exclude = {'user'}

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classses and remove labels
        """

        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Address Line 1',
            'default_street_address2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Post Code',
            'default_county': 'County',
            'default_country': 'Country'
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
