from django.shortcuts import redirect
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

def add_cart(request, item_id):
    # カートが存在したない場合は初期化
    if "cart_data" not in request.session :
        request.session["cart_data"] = []
    # POSTでカートに追加の場合はSESSIONに追加
    if request.method == "POST":
        Item = Items.objects.get(pk=item_id)
        request.session["cart_data"] += [{
            'item_title': Item.title ,
            'amount': 1
        }]
    return redirect("items:list")

def detail_add_cart(request, item_id):
    # カートが存在したない場合は初期化
    if "cart_data" not in request.session :
        request.session["cart_data"] = []
    # POSTでカートに追加の場合はSESSIONに追加
    if request.method == "POST":
        Item = Items.objects.get(pk=item_id)
        quantity = request.POST.get("quantity", default=0)
        request.session["cart_data"] += [{
            'item_title': Item.title ,
            'amount': quantity
        }]
    return redirect("items:list")