from django.db import models
from datetime import datetime

# Create your models here.
class Items(models.Model):
    class Meta:
        db_table = "items"

    title = models.CharField(verbose_name="タイトル", max_length=255, blank=True)
    price = models.IntegerField(verbose_name="価格", blank=True)
    image = models.ImageField(verbose_name="商品画像", blank=True)
    description = models.TextField(verbose_name="説明", max_length=1000, blank=True)

    def __str__(self):
        return self.title

class Carts(models.Model):
    class Meta:
        db_table = "carts"

    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.id

class CartItems(models.Model):
    class Meta:
        db_table = "cart_items"

    cart = models.ForeignKey(Carts, verbose_name="カート", on_delete=models.CASCADE)
    item = models.ForeignKey(Items, verbose_name="商品", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="数量", blank=True)

    def __str__(self):
        return self.id

