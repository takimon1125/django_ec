from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from items.models import Items
from checkout.models import Checkout, CheckoutItems
from basicauth.decorators import basic_auth_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(basic_auth_required, name='dispatch')
class ManageItemsListView(ListView):
    model = Items
    template_name = "manageapp/manageapp_items_list.html"

@method_decorator(basic_auth_required, name='dispatch')
class ManageItemsCreateView(SuccessMessageMixin, CreateView):
    model = Items
    fields = ["title", "price", "image", "description"]
    template_name = "manageapp/manageapp_items_create.html"
    success_message = "登録に成功しました。"
    success_url = reverse_lazy("manageapp:manage_items_list")

@method_decorator(basic_auth_required, name='dispatch')
class ManageItemUpdateView(SuccessMessageMixin, UpdateView):
    model = Items
    fields = ["title", "price", "image", "description"]
    template_name = "manageapp/manageapp_items_update.html"
    success_message = "更新に成功しました。"
    success_url = reverse_lazy("manageapp:manage_items_list")

@method_decorator(basic_auth_required, name='dispatch')
class ManageItemDeleteView(SuccessMessageMixin, DeleteView):
    model = Items
    template_name = "manageapp/manageapp_items_delete.html"
    success_message = "削除に成功しました。"
    success_url = reverse_lazy("manageapp:manage_items_list")

@method_decorator(basic_auth_required, name='dispatch')
class ManageCheckoutListView(ListView):
    model = Checkout
    template_name = "manageapp/manageapp_checkout_list.html"

@method_decorator(basic_auth_required, name='dispatch')
class ManageCheckoutDetailView(DetailView):
    model = Checkout
    template_name = "manageapp/manageapp_checkout_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_id = kwargs.get('object').id
        checkout_items = CheckoutItems.objects.filter(checkout=checkout_id)
        context["object_list"] = checkout_items
        context["sum_price"] = sum([items.price * items.quantity for items in checkout_items])
        return context