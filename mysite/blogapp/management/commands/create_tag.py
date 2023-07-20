from django.core.management import BaseCommand
from blogapp.models import Tag


class Command(BaseCommand):
    """
    Create tag
    """
    def handle(self, *args, **options):
        self.stdout.write("Create tag")
        tags = [
            'food',
            'sport',
            'technology',
        ]
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            self.stdout.write(f'Created tag {tag.name}')
        self.stdout.write(self.style.SUCCESS('Tags created'))
