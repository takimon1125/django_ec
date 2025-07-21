from .models import CartItems

def cart_count(request):
    cart_count = CartItems.objects.filter(cart=request.session["cart_id"]).count() if "cart_id" in request.session else 0
    return {'cart_count': cart_count}