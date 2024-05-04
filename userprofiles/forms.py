from django import forms

from userprofiles.models import Documents, UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ["file"]
