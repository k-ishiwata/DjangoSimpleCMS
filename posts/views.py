from django.http import HttpResponse
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        return (
            Post.objects
                .filter(is_public=True)
                .order_by('-published_at')
        )

class DetailView(generic.DetailView):
    def get_queryset(self):
        return Post.objects.filter(is_public=True)