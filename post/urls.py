from django.urls import path

from post.views import PostDetailView

app_name = "post"

urlpatterns = [
    path("<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
]
