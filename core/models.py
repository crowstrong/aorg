from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext as _

from core.tasks import validate_national_number, validate_phone_number


class CustomUserModel(AbstractUser):
    GENDER_CHOICES = (
        ("Male", _("Чоловічий")),
        ("Female", _("Жіночий")),
        ("NA", _("Не вказано")),
    )

    name = models.CharField(max_length=100, verbose_name=_("Імʼя"))
    surname = models.CharField(max_length=100, verbose_name=_("Прізвище"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(
        max_length=15,
        verbose_name=_("Номер телефону"),
        help_text=_('Введіть номер телефону у форматі "+32xxxxxxxxx"'),
        null=True,  # Делаем поле необязательным
        blank=True,
    )
    national_number = models.CharField(
        max_length=15,
        verbose_name=_("Національний номер"),
        help_text=_('Введіть національний номер у форматі "00.00.00-000.00"'),
        validators=[
            # Добавим валидатор для проверки формата национального номера
            RegexValidator(
                regex=r"^\d{2}\.\d{2}\.\d{2}-\d{3}\.\d{2}$",
                message=_('Національний номер повинен бути у форматі "00.00.00-000.00".'),
            )
        ],
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default="NA", verbose_name=_("Стать"))
    birth_date = models.DateField(verbose_name=_("Дата рождения"), null=True, blank=True)

    def clean(self):
        super().clean()
        if self.phone_number and not self.phone_number.startswith("+32"):
            raise ValidationError({"phone_number": _('Номер телефону повинен починатися з "+32"')})

    def save(self, *args, **kwargs):
        self.clean()  # Вызываем метод clean перед сохранением
        super().save(*args, **kwargs)
        validate_phone_number.delay(self.id)
        validate_national_number.delay(self.id)
