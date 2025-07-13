from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.
class CheckoutCreateView(TemplateView):
    template_name = "checkout/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_list = self.request.session.get("cart_data", default = []) 
        context["cart_list"] = cart_list
        context["cart_sum_price"] = sum([cart["price"] * cart["quantity"] for cart in cart_list])
        return context

def delete_cart(request, index):
    # 特定のcartのindexから削除
    if request.method == "POST":
        del request.session["cart_data"][index]
        request.session.save()
    return redirect("checkout:checkout")