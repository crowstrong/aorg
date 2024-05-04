from django.views.generic import CreateView

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback/feedback_create.html"

    def form_valid(self, form):
        # Additional processing if needed
        return super().form_valid(form)
