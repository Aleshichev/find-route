from django.db import models

# Create your models here.
from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Назва маршруту")

    travel_times = models.PositiveSmallIntegerField(verbose_name='Загальний час у дорозі')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_from_city_set',
                                  verbose_name='З якого міста'
                                  )
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                  related_name='route_to_city_set',
                                  verbose_name='В яке місто'
                                  )

    trains = models.ManyToManyField('trains.Train',
                                    verbose_name='Список поїздів')

    def __str__(self):
        return f'Маршрут {self.name} з міста {self.from_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'
        ordering = ['travel_times']
        
    # def clean(self):
    #     """Предварительная проверка данных"""
    #     if self.from_city == self.to_city:
    #         raise ValidationError("Змінити місто прибуття")
    #     qs = Train.objects.filter(
    #         from_city=self.from_city, to_city=self.to_city, travel_time=self.travel_time
    #     ).exclude(pk=self.pk)
    #     # Train = self.__class__
    #     if qs.exists() or self.travel_time <= 0:
    #         raise ValidationError("Змінить час")

    #     # if self.travel_time <= 0:
    #     #     raise ValidationError("Змінить час")

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)
