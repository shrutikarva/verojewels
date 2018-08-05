from django.urls import path
from . import views
urlpatterns = [
    path('', views.products, name='product'),
    path('<str:ptype>/', views.product_details, name='details'),
]