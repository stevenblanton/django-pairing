from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = [
        'posts',
    ]

