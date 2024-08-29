from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('my_shop/', views.my_shop_view, name='my_shop'),
]
