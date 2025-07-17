from django.urls import path
from items import views

app_name = "items"
urlpatterns = [
    path('', views.ItemsListView.as_view(), name = "list"),
    path('<int:pk>/', views.ItemsDetailView.as_view(), name = "detail"),
    path('addcart/<int:item_id>/', views.add_cart, name = "addcart"),
    path('addcart/detail/<int:item_id>/', views.detail_add_cart, name = "detail_addcart"),
]