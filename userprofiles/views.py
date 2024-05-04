from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View

from userprofiles.forms import DocumentForm, UserProfileForm
from userprofiles.models import Documents, UserProfile


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = request.user.profile
        return render(request, "profile.html", {"profile": profile})


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profile_update.html"
    success_url = "/profile/"


class DocumentListView(LoginRequiredMixin, ListView):
    model = Documents
    template_name = "document_list.html"
    context_object_name = "documents"

    def get_queryset(self):
        return Documents.objects.filter(user=self.request.user)


class DocumentUploadView(LoginRequiredMixin, CreateView):
    model = Documents
    form_class = DocumentForm
    template_name = "document_upload.html"
    success_url = "/documents/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
