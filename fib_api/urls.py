from django.urls import path
from fib_api import views

urlpatterns = [
    path('', views.fib_number, name='fib_number'),
]
