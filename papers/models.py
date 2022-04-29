from django.db import models
from taggit.managers import TaggableManager
from papers.utility import create_uuid


class File(models.Model):
    class MimeType(models.TextChoices):
        PDF = "application/pdf"

    mimetype = models.CharField(max_length=30, choices=MimeType.choices)
    path = models.FilePathField()


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Author(name={self.name})"


class Record(models.Model):
    uuid = models.UUIDField(primary_key=True, default=create_uuid, editable=False)
    file = models.OneToOneField("File", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    authors = models.ManyToManyField("Author")
    tags = TaggableManager()
