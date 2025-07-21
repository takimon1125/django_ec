from django.shortcuts import redirect
from django.views.generic import TemplateView
from items.models import CartItems

# Create your views here.
class CheckoutCreateView(TemplateView):
    template_name = "checkout/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items_list = CartItems.objects.filter(cart__id=self.request.session["cart_id"]).select_related("item") if "cart_id" in self.request.session else [] 
        context["cart_list"] = cart_items_list
        context["cart_sum_price"] = sum([cart.item.price * cart.quantity for cart in cart_items_list])
        return context

def delete_cart(request, item_id):
    # 特定のcartのindexから削除
    if request.method == "POST":
        cart_list = CartItems.objects.filter(cart__id=request.session["cart_id"], item__id=item_id)
        cart_list.delete()
    return redirect("checkout:checkout")