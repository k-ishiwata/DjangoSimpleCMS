from django.http import HttpResponse
from django.views import generic

from .models import Post, Category


class IndexView(generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        
        posts = Post.objects.filter(is_public=True)

        # カテゴリーが指定されていたら条件追加
        if ('category' in self.kwargs):
            posts = posts.filter(category=self.kwargs['category'])

        posts = posts.order_by('-published_at').prefetch_related('category')

        return posts


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = 'お知らせ'

        context['categories'] = Category.objects.values('id', 'title')

        # 現在のページのカテゴリータイトル
        if ('category' in self.kwargs):
            result = next(
                item for item in context['categories']
                if item['id'] == self.kwargs['category']
            )
            context['title'] = result['title']

        return context


class DetailView(generic.DetailView):
    def get_queryset(self):
        return Post.objects.filter(is_public=True)