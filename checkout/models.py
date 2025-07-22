from django.db import models

# Create your models here.
class Checkout(models.Model):
    class Meta:
        db_table = "checkout"

    email = models.EmailField(verbose_name="タイトル", max_length=255, blank=True)

    def __str__(self):
        return self.email