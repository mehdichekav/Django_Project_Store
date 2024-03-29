from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    is_expired = models.BooleanField(default=False)
    logical_delete = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        abstract = True

    def expired(self):
        self.is_expired = True
        self.save()

    def log_delete(self):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()


class TestModel(BaseModel):
    pass


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    update = models.DateTimeField(auto_now=True, verbose_name=_('update'))
