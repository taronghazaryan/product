from django.urls import path
from .views import ProductApi

app_name = 'product'

urlpatterns = [
    path('add/', ProductApi.as_view()),
    path('get/', ProductApi.as_view()),
]