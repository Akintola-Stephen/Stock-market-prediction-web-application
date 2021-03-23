from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.index, name='predicting-stock'),
    path('stock-list/', views.stock_list, name='stock-list'),
]
