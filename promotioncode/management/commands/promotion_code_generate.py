import random, string
from django.core.management.base import BaseCommand
from promotioncode.models import PromotionCode

class Command(BaseCommand):
    help = "プロモーションコードを10個生成するコマンドです"
    
    def handle(self, *args, **options):
        # プロモーションコードを10個作成
        print("プロモーションコードを10個生成します。")
        for _ in range(10):
            randomlst = [random.choice(string.ascii_letters + string.digits) for _ in range(7)]
            promotion_code = "".join(randomlst)
            discount_price = random.randint(100, 1000)
            promotion_code = PromotionCode(code=promotion_code, discount_price=discount_price)
            promotion_code.save()
            print(promotion_code)