from django.contrib import admin
from .models import UserProfile, Faq


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'default_phone_number', 'default_postcode',
              'default_town_or_city', 'default_street_address1',
              'default_street_address2', 'default_county', 'default_country')


class FaqAdmin(admin.ModelAdmin):
    fields = ('collapse_id', 'title', 'body')
    list_display = ('title', 'collapse_id')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Faq, FaqAdmin)
