from django import forms

from core.models import CustomUserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ["username", "name", "surname", "email", "phone_number", "national_number", "gender", "birth_date"]
