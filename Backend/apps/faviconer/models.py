from django.db import models

from apps.account.models import UserProfile


class Favicon(models.Model):
    id = models.CharField(primary_key=True, max_length=500)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    source_url = models.URLField(default=None, null=True)
    destination_url = models.URLField(default=None, null=True)
    size = models.IntegerField(default=None, null=True)

    def __unicode__ (self) -> any:
        return self.id