import uuid
from django.db import models


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения", auto_now=True, null=True, blank=True
    )

    class Meta:
        abstract = True


class Directory(Base):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=150,
        null=True,
        blank=True,
        db_index=True,
    )
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}"

    @classmethod
    def find_by_name(cls, name: str) -> object | None:
        return cls.objects.filter(name=name).first()

    @classmethod
    def find_by_id(cls, id: models.UUIDField) -> object | None:
        return cls.objects.filter(id=id).first()

    class Meta:
        abstract = True
