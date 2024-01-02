from django.db import models


class Link(models.Model):
    original_link = models.URLField(unique=True)
    short_link = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.original_link
