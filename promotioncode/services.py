from promotioncode.models import PromotionCode


class PromotionCodeService:

    @staticmethod
    def validate_promotion_code(promotion_code):
        # 存在する場合はプロモーションコードのデータを取得
        promotioncode = PromotionCode.objects.filter(code=promotion_code, is_used=False).first()
        if not promotioncode:
            return [], "プロモーションコードが存在しません。"
        
        return promotioncode, None

    @staticmethod
    def used_promotion_code(promotioncode):
        if promotioncode:
            promotioncode.is_used = True
            promotioncode.save()