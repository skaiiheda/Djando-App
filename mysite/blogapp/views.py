from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView

from .models import Article


class ArticlesListView(ListView):
    queryset = Article.objects.defer("content").select_related("author", "category").prefetch_related("tags")
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article


class LatestArticlesFeed(Feed):
    title = "Blog articles (latest)"
    description = "Updates on changes and additions blog articles"
    link = reverse_lazy("blogapp:articles")

    def items(self):
        return Article.objects.defer("content").select_related("author", "category").order_by("-pub_date")[:5]

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.content[:200]
