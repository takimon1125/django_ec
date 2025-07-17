from .models import CartsItems

def cart_count(request):
    cart_count = len(CartsItems.objects.filter(carts=request.session["cart_id"])) if "cart_id" in request.session else 0
    return {'cart_count': cart_count}