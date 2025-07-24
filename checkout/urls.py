from django.urls import path
from checkout import views

app_name = "checkout"
urlpatterns = [
    path('', views.CheckoutCreateView.as_view(), name = "checkout_create"),
    path('delete/<int:item_id>/', views.delete_cart, name = "checkout_delete"),
]