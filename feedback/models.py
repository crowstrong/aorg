from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    TOPIC_CHOICES = [
        ("service_info_request", _("Запит інформації про послуги Amodius")),
        ("partnership", _("Співпраця/партнерство з Amodius")),
        ("communication_department", _("Запит до відділу комунікацій/преси")),
        ("other", _("Інше")),
    ]

    full_name = models.CharField(max_length=100, verbose_name=_("Ім'я та Прізвище"))
    phone_number = PhoneNumberField(verbose_name=_("Номер телефону"))
    email = models.EmailField(verbose_name=_("Email"))
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES, verbose_name=_("Тема"))
    comment = models.TextField(verbose_name=_("Коментарій"))

    def __str__(self):
        return f"Дякуємо {self.name}, ми звʼяжемося з Вами якомога швидше."
