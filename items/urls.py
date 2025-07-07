from django.urls import path, include
from items import views

urlpatterns = [
    path('', views.ItemsListView.as_view()),
]