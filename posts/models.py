from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, db_comment='タイトル', verbose_name='タイトル')
    body = models.TextField(db_comment='内容', verbose_name='内容')
    is_public = models.BooleanField(default=True, db_comment='表示・非表示', verbose_name='公開')
    published_at = models.DateTimeField(db_comment='公開日', verbose_name='公開日')

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'