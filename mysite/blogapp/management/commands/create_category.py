from django.core.management import BaseCommand
from blogapp.models import Category


class Command(BaseCommand):
    """
    Create category
    """
    def handle(self, *args, **options):
        self.stdout.write("Create category")
        categories = [
            'Literature',
            'Movies',
            'History',
        ]
        for category in categories:
            category, created = Category.objects.get_or_create(name=category)
            self.stdout.write(f'Created category {category.name}')
        self.stdout.write(self.style.SUCCESS('Categories created'))
