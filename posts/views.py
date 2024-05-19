from django.http import HttpResponse
from django.views import generic

from .models import Post, Category, Tag


class IndexView(generic.ListView):
    paginate_by = 10

    def get_queryset(self):

        posts = Post.objects.filter(is_public=True)

        # カテゴリーが指定されていたら条件追加
        if ('category' in self.kwargs):
            posts = posts.filter(category=self.kwargs['category'])

        # タグが指定されていたら条件追加
        if ('tag' in self.kwargs):
            posts = posts.filter(tags=self.kwargs['tag'])

        posts = posts.order_by('-published_at').prefetch_related('category', 'tags')

        return posts


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ナビゲーション用カテゴリー
        context['categories'] = Category.objects.values('id', 'title')

        # ナビゲーション用タグ
        context['tags'] = Tag.objects.values('id', 'title')

        # タイトルの制御
        context['title'] = 'お知らせ'

        if ('category' in self.kwargs):
            result = next(
                item for item in context['categories']
                if item['id'] == self.kwargs['category']
            )
            context['title'] = result['title']

        if ('tag' in self.kwargs):
            result = next(
                item for item in context['tags']
                if item['id'] == self.kwargs['tag']
            )
            context['title'] = result['title']

        return context


class DetailView(generic.DetailView):
    def get_queryset(self):
        return Post.objects.filter(is_public=True)