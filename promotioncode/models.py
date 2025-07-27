from django.db import models

# Create your models here.
class PromotionCode(models.Model):
    class Meta:
        db_table = "promotioncode"

    code = models.CharField(verbose_name="プロモーションコード", max_length=7, unique=True)
    discount_price = models.IntegerField(verbose_name="割引額")
    is_used = models.BooleanField(verbose_name="使用済みフラグ", default=False)

    def __str__(self):
        return f"{self.code} - {self.discount_price}円"