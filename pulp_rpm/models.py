from __future__ import unicode_literals

from django.db import models

from pulp.models import ContentUnit


class NEVRAPackage(ContentUnit):
    NEVRA_FIELDS = ('name', 'epoch', 'version', 'release', 'arch')
    KEY_FIELDS = NEVRA_FIELDS + ('checksum', 'checksumtype')

    name = models.CharField(max_length=127)
    epoch = models.CharField(max_length=63)
    version = models.CharField(max_length=63)
    release = models.CharField(max_length=63)
    arch = models.CharField(max_length=63)
    checksum = models.CharField(max_length=63)
    checksumtype = models.CharField(max_length=63)

    class Meta:
        abstract = True

    def __str__(self):
        field_values = [getattr(self, field) for field in self.NEVRA_FIELDS]
        return '-'.join(field_values)


class RPM(NEVRAPackage):
    pass


class SRPM(NEVRAPackage):
    pass
