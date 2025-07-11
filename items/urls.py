from django.urls import path
from items import views

app_name = "items"
urlpatterns = [
    path('', views.ItemsListView.as_view(), name = "list"),
    path('<int:pk>/', views.ItemsDetailView.as_view(), name = "detail"),
]