from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Номер потягу")

    travel_time = models.PositiveSmallIntegerField(verbose_name="Час в дорозі")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="from_city_set",
        verbose_name="З якого міста",
    )
    to_city = models.ForeignKey(
        "cities.City",
        on_delete=models.CASCADE,
        related_name="to_city_set",
        verbose_name="В яке місто",
    )

    def __str__(self):
        return f"Потяг № {self.name} з м. {self.from_city}"

    class Meta:
        verbose_name = "Потяг"
        verbose_name_plural = "Поїзди"
        ordering = ["from_city"]

    def clean(self):
        """Предварительная проверка данных"""
        if self.from_city == self.to_city:
            raise ValidationError("Змінити місто прибуття")
        qs = Train.objects.filter(
            from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time
        ).exclude(pk=self.pk)
        # Train = self.__class__
        if qs.exists() or self.travel_time <= 0:
            raise ValidationError("Змінить час")

        # if self.travel_time <= 0:
        #     raise ValidationError("Змінить час")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
