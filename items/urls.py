from django.urls import path, include
from items import views

urlpatterns = [
    path('', views.ItemsListView.as_view(), name = "items_list"),
    path('<int:pk>/', views.ItemsDetailView.as_view(), name = "items_detail"),
]