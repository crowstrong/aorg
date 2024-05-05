import importlib
import logging

from celery import shared_task
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)


@shared_task
def validate_phone_number(user_id):
    module_name = "core.models"
    try:
        custom_user_module = importlib.import_module(module_name)
        CustomUserModel = getattr(custom_user_module, "CustomUserModel")
        user = CustomUserModel.objects.get(pk=user_id)
        user.clean()
        user.save()
    except CustomUserModel.DoesNotExist:
        logger.error(_(f"Пользователь с ID {user_id} не найден"))
    except Exception as e:
        logger.error(_(f"Ошибка при валидации номера телефона пользователя {user_id}: {e}"))


@shared_task
def validate_national_number(user_id):
    module_name = "core.models"
    try:
        custom_user_module = importlib.import_module(module_name)
        CustomUserModel = getattr(custom_user_module, "CustomUserModel")
        user = CustomUserModel.objects.get(id=user_id)
        national_number = user.national_number
        validator = RegexValidator(
            regex=r"^\d{2}\.\d{2}\.\d{2}-\d{3}\.\d{2}$",
            message=_('Національний номер повинен бути у форматі "00.00.00-000.00".'),
        )
        validator(national_number)  # Вызываем валидатор
    except CustomUserModel.DoesNotExist:
        logger.error(_(f"Пользователь с ID {user_id} не найден"))
    except ValidationError as e:
        logger.error(_(f"Ошибка валидации национального номера пользователя {user_id}: {e}"))
    except Exception as e:
        logger.error(_(f"Произошла ошибка при выполнении задачи для пользователя {user_id}: {e}"))
