from django import forms
from django.utils.translation import gettext as _

from subscription.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["subscription_type", "price"]
        labels = {
            "subscription_type": _("Тип підписка"),
            "price": _("Ціна"),
        }

    def clean(self):
        cleaned_data = super().clean()
        subscription_type = cleaned_data.get("subscription_type")

        # Устанавливаем цену в зависимости от выбранного типа подписки
        if subscription_type:
            if subscription_type == "individual_1_month":
                cleaned_data["price"] = 29.99
            elif subscription_type == "individual_1_year":
                cleaned_data["price"] = 199.99
            elif subscription_type == "family_1_month":
                cleaned_data["price"] = 49.99
            elif subscription_type == "family_1_year":
                cleaned_data["price"] = 299.99

        return cleaned_data
