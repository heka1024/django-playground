from django import models


class BaseQuerySet(models.QuerySet):
    def created_before(self, date):
        return self.filter(created_at__lt=date)

    def created_after(self, date):
        return self.filter(created_at__gt=date)

    def created_between(self, start, end):
        return self.filter(created_at__range=(start, end))

    def updated_before(self, date):
        return self.filter(updated_at__lt=date)

    def updated_after(self, date):
        return self.filter(updated_at__gt=date)

    def updated_between(self, start, end):
        return self.filter(updated_at__range=(start, end))


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseQuerySet.as_manager()

    class Meta:
        abstract = True

    def update(self, **kwargs):
        """update method를 위한 단축키"""
        return self.__class__.objects.filter(pk=self.pk).update(**kwargs)

    @property
    def is_new_record(self) -> bool:
        """
        새로 생성된 레코드라면 True를 반환
        이미 DB에 저장된 레코드라면 False를 반환
        """
        return self.pk is None
