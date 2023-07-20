from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author")
    bio = models.TextField(null=False, blank=True, verbose_name="Biography")

    def __str__(self) -> str:
        return f"Author(name={self.name!r})"


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name="Category")

    def __str__(self) -> str:
        return f"Category(name={self.name!r})"


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="Tag")

    def __str__(self) -> str:
        return f"Tag(name={self.name!r})"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(null=False, blank=True, verbose_name="Article")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Date of publication of the article")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    tags = models.ManyToManyField(Tag, related_name='articles', verbose_name="tags")

    def get_absolute_url(self):
        return reverse("blogapp:article", kwargs={"pk": self.pk})
