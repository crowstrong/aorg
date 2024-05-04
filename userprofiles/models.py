from django.core.validators import FileExtensionValidator
from django.db import models

from core.models import CustomUserModel


class Documents(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="uploaded_documents")
    file = models.FileField(
        upload_to="documents/", validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "pdf"])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} uploaded by {self.user.username}"

    class Meta:
        ordering = ["-uploaded_at"]


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="media/avatars/", null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
