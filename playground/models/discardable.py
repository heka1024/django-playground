from django.db import models
from django.utils import timezone

from .base_model import BaseModel, BaseModelQuerySet


class DiscardableQuerySet(BaseModelQuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class Discardable(BaseModel):
    """Soft delete를 위한 abstract model"""
    discarded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def discard(self):
        self.discarded_at = timezone.now()
        self.save(update_fields=['discarded_at'])

    def restore(self):
        self.discarded_at = None
        self.save(update_fields=['discarded_at'])

    @property
    def is_discarded(self) -> bool:
        return self.discarded_at is not None
