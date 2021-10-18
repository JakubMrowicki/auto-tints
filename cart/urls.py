from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_to_cart/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('edit_item/<item_id>/', views.edit_item, name='edit_item'),
]
