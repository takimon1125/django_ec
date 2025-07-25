from django.contrib import admin
from .models import Checkout, CheckoutItems

# Register your models here.
admin.site.register(CheckoutItems)
admin.site.register(Checkout)