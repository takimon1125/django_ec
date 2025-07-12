from django.urls import path
from manageapp import views

app_name = "manageapp"
urlpatterns = [
    path('items/', views.ManageItemsListView.as_view(), name = "manage_items_list"),
    path('items/create/', views. ManageItemsCreateView.as_view(), name = "manage_items_create"),
    path('items/<int:pk>/', views.ManageItemUpdateView.as_view(), name = "manage_items_update"),
    path('items/delete/<int:pk>/', views.ManageItemDeleteView.as_view(), name = "manage_items_delete"),
]