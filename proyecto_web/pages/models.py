from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=180, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to="pages/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pages"
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
