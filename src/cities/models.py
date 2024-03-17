from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Місто")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Місто"
        verbose_name_plural = "Міста"
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("cities:detail", kwargs={"pk": self.pk})

    # def clean(self):
    #     if not self.name.replace(" ", "").isalpha():
    #         raise ValidationError(None)

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)
