from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Items

# Create your views here.
class ItemsListView(ListView):
    model = Items

class ItemsDetailView(DetailView):
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Items.objects.all().order_by("-id")[0:4]
        return context