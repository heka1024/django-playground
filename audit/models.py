from django.db import models


class IPAuditLog(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True, editable=False)


class VarcharAuditLog(models.Model):
    ip = models.CharField(max_length=45, blank=True, null=False)
