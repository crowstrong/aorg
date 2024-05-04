from django.views.generic import DetailView

from .models import Post


# Create your views here.
class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
