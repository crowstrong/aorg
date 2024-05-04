from django.urls import path

from feedback.views import FeedbackCreateView

app_name = "feedback"

urlpatterns = [
    path("create/", FeedbackCreateView.as_view(), name="feedback_create"),
]
