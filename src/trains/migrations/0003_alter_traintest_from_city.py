# Generated by Django 4.0.5 on 2022-06-30 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_name'),
        ('trains', '0002_remove_traintest_travel_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traintest',
            name='from_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='cities.city', verbose_name='Из какого города'),
        ),
    ]
