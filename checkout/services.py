from django.db import transaction
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from items.models import CartItems
from .models import CheckoutItems


class CheckoutService:

    @staticmethod
    def validate_cart_items(session):
        # セッションにカートIDが存在するのか確認
        if "cart_id" not in session:
            return [], "カートが存在しません。カートに商品を追加してください。"

        # 存在する場合はカートのデータを取得して存在を確認
        cart_items = CartItems.objects.filter(cart__id=session["cart_id"]).select_related("item")
        if not cart_items:
            return [], "カートに商品がありません。カートに商品を追加してください。"
        
        return cart_items, None
    
    @staticmethod
    def create_checkout_items(checkout, cart_items):
        checkout_items = []
        total_price = 0
        # カート内の商品からチェックアウトアイテムを登録する
        for cart_item in cart_items:
            checkout_item = CheckoutItems.objects.create(
                checkout=checkout,
                title=cart_item.item.title,
                price=cart_item.item.price,
                image=cart_item.item.image,
                description=cart_item.item.description,
                quantity=cart_item.quantity,
            )
            checkout_items.append(checkout_item)
            total_price += cart_item.item.price * cart_item.quantity
        return checkout_items, total_price
    
    @staticmethod
    def process_checkout(form, session):
        # カートアイテムのあるのかを確認
        cart_items, error_message = CheckoutService.validate_cart_items(session)
        if error_message:
            return None, None, error_message
        
        with transaction.atomic():
            # チェックアウトの作成
            checkout = form.save()
            # チェックアウトアイテムの作成
            checkout_items, total_price = CheckoutService.create_checkout_items(checkout, cart_items)
            # セッションからカートIDを削除
            if "cart_id" in session:
                del session["cart_id"]
        
        return checkout, checkout_items, total_price


class EmailService:

    @staticmethod
    def send_checkout_email(checkout, checkout_items, total_price):
        subject = "TakimonECのご注文"

        # テキストメールの作成
        text_content = render_to_string(
            "emails/checkout_email.txt",
            context={
                "checkout": checkout,
                "checkout_item_list": checkout_items,
                "total_price": total_price
            },
        )

        # HTMLメールの作成
        html_content = render_to_string(
            "emails/checkout_email.html",
            context={
                "checkout": checkout,
                "checkout_item_list": checkout_items,
                "total_price": total_price
            },
        )

        # メール送信
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [checkout.email]

        email = EmailMultiAlternatives(
            subject,
            text_content,
            from_email,
            recipient_list
        )
        email.attach_alternative(html_content, "text/html")
        email.send()