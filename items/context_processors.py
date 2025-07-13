def cart_count(request):
    cart_count = len(request.session.get("cart_data", default = []))
    return {'cart_count': cart_count}