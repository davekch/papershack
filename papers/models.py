from __future__ import annotations
from django.db import models
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase, Tag
from papers.utility import create_uuid


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Author(name={self.name})"


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    """through-class for tags that are tied to models with a uuid as primary key"""

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


def file_path(instance: Record, filename: str):
    if not instance.uuid:
        instance.save()
    return f"{str(instance.uuid)}/{filename}"


class Record(models.Model):
    uuid = models.UUIDField(primary_key=True, default=create_uuid, editable=False)
    file = models.FileField(upload_to=file_path, null=True, blank=True)
    title = models.CharField(max_length=300)
    authors = models.ManyToManyField("Author")
    tags = TaggableManager(through=UUIDTaggedItem)

    def delete(self) -> tuple[int, dict[str, int]]:
        deleted = super().delete()
        # clean up unreferenced tags
        Tag.objects.annotate(n_references=Count("papers_uuidtaggeditem_items")).filter(
            n_references=0
        ).delete()
        return deleted
