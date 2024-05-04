from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from core.models import CustomUserModel


class Subscription(models.Model):
    SUBSCRIPTION_CHOICES = [
        ("individual_1_month", _("Індивідуальне членство на 1 місяць")),
        ("individual_1_year", _("Індивідуальне членство на 1 рік")),
        ("family_1_month", _("Сімейне членство на 1 місяць")),
        ("family_1_year", _("Сімейне членство на 1 рік")),
    ]

    user = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name="subscriptions", verbose_name=_("Користувач")
    )
    subscription_type = models.CharField(max_length=50, choices=SUBSCRIPTION_CHOICES, verbose_name=_("Тип підписка"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Ціна"))
    start_date = models.DateField(auto_now_add=True, verbose_name=_("Дата початку підписки"))
    end_date = models.DateField(verbose_name=_("Дата закінчення підписки"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активна"))

    def __str__(self):
        return f"{self.subscription_type} для {self.user.username}"

    def save(self, *args, **kwargs):
        if self.subscription_type in ["individual_1_month", "family_1_month"]:
            # Если подписка на месяц, устанавливаем дату окончания подписки на 30 дней после даты начала
            self.end_date = self.start_date + timezone.timedelta(days=30)
        elif self.subscription_type in ["individual_1_year", "family_1_year"]:
            # Если подписка на год, устанавливаем дату окончания подписки на 365 дней после даты начала
            self.end_date = self.start_date + timezone.timedelta(days=365)

        super().save(*args, **kwargs)
