from django.urls import path
from checkout import views

app_name = "checkout"
urlpatterns = [
    path('', views.CheckoutCreateView.as_view(), name = "checkout"),
    path('delete/<int:index>/', views.delete_cart, name = "checkout_delete"),
]