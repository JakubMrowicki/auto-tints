from django.urls import path
from . import views

urlpatterns = [
    path('pages/faq/', views.faq, name='faq'),
    path('profile/', views.profile, name='profile'),
]
