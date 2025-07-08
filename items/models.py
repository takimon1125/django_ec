from django.db import models

# Create your models here.
class Items(models.Model):
    class Meta:
        db_table = "item"

    title = models.CharField(verbose_name="タイトル", max_length=255, blank=True)
    price = models.IntegerField(verbose_name="価格", blank=True)
    image = models.ImageField(verbose_name="商品画像", blank=True)
    description = models.ImageField(verbose_name="商品説明", max_length=1000, blank=True)

    def __str__(self):
        return self.title