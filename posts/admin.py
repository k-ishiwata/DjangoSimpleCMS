from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'published_at']
    search_fields = ['title', 'body']

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['title', 'created_at', 'updated_at']

admin.site.register(Category, CategoryAdmin)