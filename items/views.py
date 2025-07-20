from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Items, Carts, CartItems

# Create your views here.
class ItemsListView(ListView):
    model = Items

class ItemsDetailView(DetailView):
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Items.objects.all().order_by("-id")[0:4]
        return context

def add_cart(request, item_id):
    if request.method == "POST":
        # item_idからitemを取得
        item = Items.objects.get(pk=item_id)
        # カートIDがセッションにあればカートを取得。なければ新規に作成
        cart = Carts.objects.get(pk=request.session["cart_id"])  if "cart_id" in request.session else Carts.objects.create()
        # sessionにカートIDを入れる
        request.session["cart_id"] = cart.id
        # カートが存在する場合はカートIDに紐づくデータを更新
        cart_item, created = CartItems.objects.get_or_create(cart=cart, item=item, defaults={'quantity': 1})
        if not created:
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
    return redirect("items:list")

def detail_add_cart(request, item_id):
    if request.method == "POST":
        # item_idからitemを取得
        item = Items.objects.get(pk=item_id)
        # カートIDがセッションにあればカートを取得。なければ新規に作成
        cart = Carts.objects.get(pk=request.session["cart_id"])  if "cart_id" in request.session else Carts.objects.create()
        # sessionにカートIDを入れる
        request.session["cart_id"] = cart.id
        # 数量をpostから取得
        quantity = int(request.POST.get("quantity", default=0) or 0)
        # カートが存在する場合はカートIDに紐づくデータを更新
        cart_item, created = CartItems.objects.get_or_create(cart=cart, item=item, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity = cart_item.quantity + quantity
            cart_item.save()
    return redirect("items:list")