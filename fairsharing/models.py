from django.db import models


# Create your models here.
class FairsharingRecord(models.Model):
    name = models.TextField(blank=False)
    abbreviation = models.CharField(max_length=128)
    doi = models.TextField(max_length=27, blank=True, null=True)
    homepage = models.URLField(blank=False)
    description = models.TextField()

    # TODO: Add JSON field and validate on save


    def __unicode__(self):
        return self.name
