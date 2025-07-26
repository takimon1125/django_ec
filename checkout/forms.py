from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ["firstname", "lastname", "username", "email", "address1", "address2", "country", "state", "zip", "card_name", "card_number", "card_expiration", "card_cvv", "promotion_code"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 全ての必須フィールドに対して一括で設定する例
        for _, field in self.fields.items():
            if field.required: # 必須フィールドの場合
                field.error_messages['required'] = f'{field.label}は必須です。'