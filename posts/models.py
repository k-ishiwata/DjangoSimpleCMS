from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='タイトル')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')
    
    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name='タイトル')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='登録日')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')
    
    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='タイトル')
    body = models.TextField(verbose_name='内容')
    is_public = models.BooleanField(default=True, verbose_name='公開')
    published_at = models.DateTimeField(verbose_name='公開日')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name ='カテゴリ')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True, verbose_name ='タグ')

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'

    def __str__(self):
        return self.title
    
    def tag_list(self):
        return ','.join([i.title for i in self.tags.all()])
