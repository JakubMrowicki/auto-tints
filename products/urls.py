from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='detail_page'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>', views.edit_product, name='edit_product'),
]
