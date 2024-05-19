from django.contrib import admin

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'get_tags', 'published_at']
    search_fields = ['title', 'body']

    def get_queryset(self, request):
        query = super().get_queryset(request)
        return query.prefetch_related('category', 'tags')

    def get_tags(self, obj):
        return ','.join([i.title for i in obj.tags.all()])

    get_tags.short_description = 'タグ'


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['title', 'created_at', 'updated_at']

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display  = ['title', 'created_at', 'updated_at']

admin.site.register(Tag, TagAdmin)