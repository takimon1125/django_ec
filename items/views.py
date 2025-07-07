from django.shortcuts import render
from django.views.generic import ListView
from .models import Items

# Create your views here.
class ItemsListView(ListView):
    template_name = "items/items_list"
    model = Items