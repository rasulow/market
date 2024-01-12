from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete-category'),
    
    path('create-product/', views.create_product, name='create-product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete-product'),
    
    path('bill/', views.bill, name='bill'),
    path('create-bill/', views.create_bill, name='create-bill')
]