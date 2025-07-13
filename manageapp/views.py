from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from items.models import Items
from basicauth.decorators import basic_auth_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(basic_auth_required, name='dispatch')
class ManageItemsListView(ListView):
    model = Items
    template_name = "manageapp/manageapp_list.html"

@method_decorator(basic_auth_required, name='dispatch')
class ManageItemsCreateView(SuccessMessageMixin, CreateView):
    model = Items
    fields = ["title", "price", "image", "description"]
    template_name = "manageapp/manageapp_create.html"
    success_message = "登録に成功しました。"
    success_url = reverse_lazy("manageapp:manage_items_list")

@method_decorator(basic_auth_required, name='dispatch')
class ManageItemUpdateView(SuccessMessageMixin, UpdateView):
    model = Items
    fields = ["title", "price", "image", "description"]
    template_name = "manageapp/manageapp_update.html"
    success_message = "更新に成功しました。"
    success_url = reverse_lazy("manageapp:manage_items_list")

@method_decorator(basic_auth_required, name='dispatch')
class ManageItemDeleteView(SuccessMessageMixin, DeleteView):
    model = Items
    template_name = "manageapp/manageapp_delete.html"
    success_message = "削除に成功しました。"
    success_url = reverse_lazy("manageapp:manage_items_list")