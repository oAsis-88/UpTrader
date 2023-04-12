from django.db import models


class Paragraph(models.Model):
    title = models.CharField(max_length=64)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return f"/{self.title}/"

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title} ({self.id})"

    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункты"
