from django.contrib import admin
from .models import Author, Category, Tag, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = "name", "bio"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ["name"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = "title", "content", "pub_date", "author_verbose"

    def get_queryset(self, request):
        return Article.objects.select_related("author").prefetch_related("tags")

    def author_verbose(self, obj: Article) -> str:
        return obj.author.name
