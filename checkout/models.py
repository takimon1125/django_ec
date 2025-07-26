from django.db import models

# Create your models here.
class Checkout(models.Model):
    COUNTRY_CHOICES = (
        ('', '選択してください'),
        ('JP', '日本'),
    )

    STATE_CHOICES = (
        ('', '選択してください'),
        ('JP-01', '北海道'),
        ('JP-02', '青森県'),
        ('JP-03', '岩手県'),
        ('JP-04', '宮城県'),
        ('JP-05', '秋田県'),
        ('JP-06', '山形県'),
        ('JP-07', '福島県'),
        ('JP-08', '茨城県'),
        ('JP-09', '栃木県'),
        ('JP-10', '群馬県'),
        ('JP-11', '埼玉県'),
        ('JP-12', '千葉県'),
        ('JP-13', '東京都'),
        ('JP-14', '神奈川県'),
        ('JP-15', '新潟県'),
        ('JP-16', '富山県'),
        ('JP-17', '石川県'),
        ('JP-18', '福井県'),
        ('JP-19', '山梨県'),
        ('JP-20', '長野県'),
        ('JP-21', '岐阜県'),
        ('JP-22', '静岡県'),
        ('JP-23', '愛知県'),
        ('JP-24', '三重県'),
        ('JP-25', '滋賀県'),
        ('JP-26', '京都府'),
        ('JP-27', '大阪府'),
        ('JP-28', '兵庫県'),
        ('JP-29', '奈良県'),
        ('JP-30', '和歌山県'),
        ('JP-31', '鳥取県'),
        ('JP-32', '島根県'),
        ('JP-33', '岡山県'),
        ('JP-34', '広島県'),
        ('JP-35', '山口県'),
        ('JP-36', '徳島県'),
        ('JP-37', '香川県'),
        ('JP-38', '愛媛県'),
        ('JP-39', '高知県'),
        ('JP-40', '福岡県'),
        ('JP-41', '佐賀県'),
        ('JP-42', '長崎県'),
        ('JP-43', '熊本県'),
        ('JP-44', '大分県'),
        ('JP-45', '宮崎県'),
        ('JP-46', '鹿児島県'),
        ('JP-47', '沖縄県'),
    )

    class Meta:
        db_table = "checkout"

    firstname = models.CharField(verbose_name="名", max_length=100)
    lastname = models.CharField(verbose_name="姓", max_length=100)
    username = models.CharField(verbose_name="ユーザー名", max_length=255)
    email = models.EmailField(verbose_name="メールアドレス", max_length=255, blank=True)
    address1 = models.CharField(verbose_name="住所1 (番地・町)", max_length=255)
    address2 = models.CharField(verbose_name="住所2 (建物名・部屋番号)", max_length=255, blank=True)
    country = models.CharField(verbose_name="国", max_length=100, choices=COUNTRY_CHOICES)
    state = models.CharField(verbose_name="県", max_length=100, choices=STATE_CHOICES)
    zip = models.CharField(verbose_name="郵便番号", max_length=20)

    card_name = models.CharField(verbose_name="カード名義", max_length=255)
    card_number = models.CharField(verbose_name="カード番号", max_length=20)
    card_expiration = models.CharField(verbose_name="有効期限", max_length=20)
    card_cvv = models.CharField(verbose_name="CVV", max_length=4)

    promotion_code = models.CharField(verbose_name="プロモーションコード", max_length=7, blank=True)
    discount_price = models.IntegerField(verbose_name="割引額", default=0, blank=True)

    created_at = models.DateTimeField(verbose_name="注文日時", auto_now_add=True)

    def __str__(self):
        return self.lastname + self.firstname


class CheckoutItems(models.Model):
    class Meta:
        db_table = "checkout_items"

    checkout = models.ForeignKey(Checkout, verbose_name="購入明細", on_delete=models.CASCADE, related_name="CheckoutItems")
    title = models.CharField(verbose_name="タイトル", max_length=255)
    price = models.IntegerField(verbose_name="価格")
    image = models.ImageField(verbose_name="商品画像")
    description = models.TextField(verbose_name="説明")
    quantity = models.IntegerField(verbose_name="数量")

    def __str__(self):
        return f"{self.checkout.id} - {self.title} ({self.quantity}個)"