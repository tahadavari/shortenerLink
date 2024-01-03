from django.db import models

from shortener.utils.qr_creator import QrCreator
from shortener.utils.shortener_link import ShortenerLink


class Link(models.Model):
    original_link = models.URLField()
    short_link = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='static/qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.original_link


