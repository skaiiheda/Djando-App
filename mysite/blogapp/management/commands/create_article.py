from typing import Sequence

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from blogapp.models import Article, Author, Category, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Create articles with author, categories and tags')
        author = Author.objects.get(name='admin')
        category = Category.objects.get(name='Literature')
        # tag = Tag.objects.get(name='technology')
        tags: Sequence[Tag] = Tag.objects.all()
        # products: Sequence[Product] = Product.objects.defer("description", "price", "created_at").all()
        # products: Sequence[Product] = Product.objects.only("id").all()
        article, created = Article.objects.get_or_create(
            title='Future',
            author=author,
            category=category,
        )
        for tag in tags:
            article.tags.add(tag)
        article.save()
        self.stdout.write(f'Created article {article}')
