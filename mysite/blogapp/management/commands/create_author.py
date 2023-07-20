from django.core.management import BaseCommand
from blogapp.models import Author


class Command(BaseCommand):
    """
    Create author
    """
    def handle(self, *args, **options):
        self.stdout.write("Create author")
        authors_names = [
            'admin',
            'sam',
            'dan',
        ]
        for author_name in authors_names:
            author, created = Author.objects.get_or_create(name=author_name)
            self.stdout.write(f'Created author {author.name}')
        self.stdout.write(self.style.SUCCESS('Authors created'))
