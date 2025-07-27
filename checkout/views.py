from django.shortcuts import redirect, render
from django.views.generic import CreateView
from items.models import CartItems
from .models import Checkout
from .forms import CheckoutForm
from promotioncode.models import PromotionCode
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from checkout.services import CheckoutService, EmailService

# Create your views here.
class CheckoutCreateView(SuccessMessageMixin, CreateView):
    template_name = "checkout/checkout.html"
    model = Checkout
    form_class = CheckoutForm
    success_message = "購入ありがとうございます。"
    success_url = reverse_lazy("items:list")

    def post(self, request, *args, **kwargs):
        # postでプロモーションコードの適用をおされたときの処理
        if "apply_promotion_code" in request.POST:
            promotioncode = PromotionCode.objects.filter(code=request.POST.get("promotion_code", None), is_used=False).first()
            if promotioncode:
                request.session['applied_promotion_code'] = promotioncode.code
                request.session['applied_promotion_discount_price'] = promotioncode.discount_price
                request.session['promotion_code_error'] = None
            else:
                request.session['applied_promotion_code'] = None
                request.session['applied_promotion_discount_price'] = None
                request.session['promotion_code_error'] = "無効なプロモーションコードです。"
            # session情報を表示するためにリダイレクトする
            return redirect(self.request.path)
        
        # 注文のフォームを処理する。
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # チェックアウト処理を実行
        checkout, cart_items, total_price_or_errormsg = CheckoutService.process_checkout(form, self.request.session)

        if checkout is None:
            # エラーが発生した場合
            form.add_error(None, total_price_or_errormsg)  # total_price_or_errormsgにはエラーメッセージが入っている
            return self.form_invalid(form)

        # メール送信
        EmailService.send_checkout_email(checkout, cart_items, total_price_or_errormsg)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # formでエラーを返す場合にバリデーションエラーを表示する
        if self.request.method == 'POST' and context['form'].is_bound and not context['form'].is_valid():
            context['form_has_errors'] = True
        else:
            context['form_has_errors'] = False

        # セッションにプロモーションコードがあれば表示する。一度取り出したらセッションを削除
        context['applied_promotion_code'] = self.request.session.pop('applied_promotion_code', None)
        context['applied_promotion_discount_price'] = self.request.session.pop('applied_promotion_discount_price', None)
        context['promotion_code_error'] = self.request.session.pop('promotion_code_error', None)

        # カート部分を表示する処理
        cart_items_list = CartItems.objects.filter(cart__id=self.request.session["cart_id"]).select_related("item") if "cart_id" in self.request.session else []
        context["cart_list"] = cart_items_list
        context["cart_sum_price"] = max(sum([cart.item.price * cart.quantity for cart in cart_items_list]) - (context['applied_promotion_discount_price'] if context['applied_promotion_discount_price'] else 0), 0)
        return context

def delete_cart(request, item_id):
    # 特定のcartのindexから削除
    if request.method == "POST":
        cart_list = CartItems.objects.filter(cart__id=request.session["cart_id"], item__id=item_id)
        cart_list.delete()
    return redirect("checkout:checkout_create")