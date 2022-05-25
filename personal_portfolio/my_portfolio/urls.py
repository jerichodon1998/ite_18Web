from my_portfolio import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
]