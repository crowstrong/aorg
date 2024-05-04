from django.contrib.auth import views as auth_views
from django.urls import path

from userprofiles.views import (DocumentListView, DocumentUploadView,
                                UserProfileUpdateView, UserProfileView)

app_name = "profiles"

urlpatterns = [
    path("profiles/", UserProfileView.as_view(), name="user_profile"),
    path("profiles/update/", UserProfileUpdateView.as_view(), name="user_profile_update"),
    path("documents/", DocumentListView.as_view(), name="document_list"),
    path("documents/upload/", DocumentUploadView.as_view(), name="document_upload"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]
